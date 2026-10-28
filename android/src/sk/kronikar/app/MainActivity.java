package sk.kronikar.app;

import android.app.Activity;
import android.content.ContentResolver;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.UriPermission;
import android.database.Cursor;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.provider.DocumentsContract;
import android.util.Base64;
import android.util.Log;
import android.webkit.JavascriptInterface;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

/**
 * Kronikár: the writing app runs in a WebView from bundled assets.
 * The "AndroidFS" bridge gives it read/write access to one folder the user picks
 * (for example a Syncthing folder) through the Storage Access Framework.
 */
public class MainActivity extends Activity {
    private static final String TAG = "Kronikar";
    private static final String START = "file:///android_asset/index.html";
    private static final int REQ_TREE = 41;
    private static final int REQ_FILE = 42;

    private WebView web;
    private ValueCallback<Uri[]> fileCallback;
    private SharedPreferences prefs;

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);
        prefs = getSharedPreferences("kronikar", MODE_PRIVATE);
        web = new WebView(this);
        web.setBackgroundColor(Color.parseColor("#E8EBEF"));
        setContentView(web);

        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setAllowFileAccess(true);
        s.setAllowFileAccessFromFileURLs(true);
        s.setAllowUniversalAccessFromFileURLs(true);
        s.setTextZoom(100);
        s.setSupportMultipleWindows(false);
        s.setMediaPlaybackRequiresUserGesture(true);

        web.addJavascriptInterface(new Bridge(), "AndroidFS");
        web.setWebViewClient(new WebViewClient() {
            @Override
            @SuppressWarnings("deprecation")
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                return openOutside(url);
            }
        });
        web.setWebChromeClient(new WebChromeClient() {
            @Override
            public boolean onShowFileChooser(WebView view, ValueCallback<Uri[]> callback, FileChooserParams params) {
                if (fileCallback != null) fileCallback.onReceiveValue(null);
                fileCallback = callback;
                try {
                    Intent i = new Intent(Intent.ACTION_OPEN_DOCUMENT);
                    i.addCategory(Intent.CATEGORY_OPENABLE);
                    i.setType("*/*");
                    startActivityForResult(i, REQ_FILE);
                } catch (Exception e) {
                    fileCallback = null;
                    return false;
                }
                return true;
            }
        });

        if (state != null) web.restoreState(state);
        else web.loadUrl(START);
    }

    /** Links to Instagram, YouTube etc. open in the phone's browser or app. */
    private boolean openOutside(String url) {
        if (url == null || url.startsWith("file:///android_asset/")) return false;
        if (url.startsWith("blob:") || url.startsWith("data:") || url.startsWith("javascript:")) return false;
        try {
            Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
            i.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            startActivity(i);
        } catch (Exception e) {
            Log.w(TAG, "cannot open " + url, e);
        }
        return true;
    }

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);
    }

    @Override
    protected void onPause() {
        // write everything to the folder before Android may stop the app
        web.evaluateJavascript("window.__androidPause && window.__androidPause()", null);
        super.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        web.evaluateJavascript("window.__androidResume && window.__androidResume()", null);
    }

    @Override
    @SuppressWarnings("deprecation")
    public void onBackPressed() {
        web.evaluateJavascript("window.__androidBack ? window.__androidBack() : false", new ValueCallback<String>() {
            @Override
            public void onReceiveValue(String handled) {
                if (!"true".equals(handled)) moveTaskToBack(true);
            }
        });
    }

    @Override
    protected void onActivityResult(int req, int res, Intent data) {
        super.onActivityResult(req, res, data);
        if (req == REQ_FILE) {
            Uri[] result = null;
            if (res == RESULT_OK && data != null && data.getData() != null) result = new Uri[]{data.getData()};
            if (fileCallback != null) fileCallback.onReceiveValue(result);
            fileCallback = null;
            return;
        }
        if (req == REQ_TREE) {
            boolean ok = false;
            if (res == RESULT_OK && data != null && data.getData() != null) {
                Uri tree = data.getData();
                try {
                    int flags = Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION;
                    getContentResolver().takePersistableUriPermission(tree, flags);
                    String old = prefs.getString("tree", null);
                    if (old != null && !old.equals(tree.toString())) {
                        try { getContentResolver().releasePersistableUriPermission(Uri.parse(old), flags); } catch (Exception ignored) { }
                    }
                    prefs.edit().putString("tree", tree.toString()).apply();
                    ok = true;
                } catch (Exception e) {
                    Log.e(TAG, "folder permission", e);
                    Toast.makeText(this, java.util.Locale.getDefault().getLanguage().matches("sk|cs") ? "Do tohto priečinka Android zápis nepovolil. Vyber iný." : "Android did not allow writing to this folder. Choose another one.", Toast.LENGTH_LONG).show();
                }
            }
            web.evaluateJavascript("window.__afsPicked && window.__afsPicked(" + ok + ")", null);
        }
    }

    /* ------------------------------------------------------------------ */
    /*  Folder access for JavaScript (runs on the WebView bridge thread)   */
    /* ------------------------------------------------------------------ */
    private Uri tree() {
        String t = prefs.getString("tree", null);
        return t == null ? null : Uri.parse(t);
    }

    private boolean permitted() {
        Uri t = tree();
        if (t == null) return false;
        for (UriPermission p : getContentResolver().getPersistedUriPermissions()) {
            if (p.getUri().equals(t) && p.isReadPermission() && p.isWritePermission()) return true;
        }
        return false;
    }

    private String rootId() { return DocumentsContract.getTreeDocumentId(tree()); }

    private Uri docUri(String id) { return DocumentsContract.buildDocumentUriUsingTree(tree(), id); }

    private static final String[] COLS = {
            DocumentsContract.Document.COLUMN_DOCUMENT_ID,
            DocumentsContract.Document.COLUMN_DISPLAY_NAME,
            DocumentsContract.Document.COLUMN_MIME_TYPE,
            DocumentsContract.Document.COLUMN_LAST_MODIFIED,
            DocumentsContract.Document.COLUMN_SIZE};

    private JSONArray children(String parentId) throws Exception {
        JSONArray out = new JSONArray();
        Uri u = DocumentsContract.buildChildDocumentsUriUsingTree(tree(), parentId);
        Cursor c = getContentResolver().query(u, COLS, null, null, null);
        if (c == null) return out;
        try {
            while (c.moveToNext()) {
                JSONObject o = new JSONObject();
                o.put("id", c.getString(0));
                o.put("name", c.getString(1));
                o.put("kind", DocumentsContract.Document.MIME_TYPE_DIR.equals(c.getString(2)) ? "directory" : "file");
                o.put("lm", c.isNull(3) ? 0 : c.getLong(3));
                o.put("size", c.isNull(4) ? 0 : c.getLong(4));
                out.put(o);
            }
        } finally {
            c.close();
        }
        return out;
    }

    private JSONObject find(String parentId, String name) throws Exception {
        JSONArray a = children(parentId);
        for (int i = 0; i < a.length(); i++) {
            JSONObject o = a.getJSONObject(i);
            if (name.equals(o.getString("name"))) return o;
        }
        return null;
    }

    /** "" = the picked folder itself, otherwise one sub-folder (e.g. "zalohy"). */
    private String dirId(String sub, boolean create) throws Exception {
        String root = rootId();
        if (sub == null || sub.isEmpty()) return root;
        JSONObject o = find(root, sub);
        if (o != null) return o.getString("id");
        if (!create) return null;
        Uri u = DocumentsContract.createDocument(getContentResolver(), docUri(root), DocumentsContract.Document.MIME_TYPE_DIR, sub);
        return u == null ? null : DocumentsContract.getDocumentId(u);
    }

    private static String mimeFor(String name) {
        String n = name.toLowerCase();
        if (n.endsWith(".json")) return "application/json";
        if (n.endsWith(".pdf")) return "application/pdf";
        if (n.endsWith(".docx")) return "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
        if (n.endsWith(".md")) return "text/markdown";
        if (n.endsWith(".txt")) return "text/plain";
        return "application/octet-stream";
    }

    private boolean writeBytes(String sub, String name, byte[] bytes) {
        try {
            String parent = dirId(sub, true);
            if (parent == null) return false;
            JSONObject o = find(parent, name);
            Uri u;
            if (o != null) u = docUri(o.getString("id"));
            else u = DocumentsContract.createDocument(getContentResolver(), docUri(parent), mimeFor(name), name);
            if (u == null) return false;
            ContentResolver cr = getContentResolver();
            OutputStream os;
            try { os = cr.openOutputStream(u, "wt"); } catch (Exception e) { os = cr.openOutputStream(u, "w"); }
            if (os == null) return false;
            try { os.write(bytes); os.flush(); } finally { os.close(); }
            return true;
        } catch (Exception e) {
            Log.e(TAG, "write " + name, e);
            return false;
        }
    }

    private class Bridge {
        @JavascriptInterface public boolean hasFolder() { return permitted(); }

        @JavascriptInterface public String folderName() {
            try {
                Cursor c = getContentResolver().query(docUri(rootId()), new String[]{DocumentsContract.Document.COLUMN_DISPLAY_NAME}, null, null, null);
                if (c != null) { try { if (c.moveToFirst()) return c.getString(0); } finally { c.close(); } }
            } catch (Exception ignored) { }
            return "Kronikár";
        }

        @JavascriptInterface public void pickFolder() {
            runOnUiThread(new Runnable() {
                @Override public void run() {
                    try {
                        Intent i = new Intent(Intent.ACTION_OPEN_DOCUMENT_TREE);
                        i.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                                | Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION | Intent.FLAG_GRANT_PREFIX_URI_PERMISSION);
                        startActivityForResult(i, REQ_TREE);
                    } catch (Exception e) {
                        web.evaluateJavascript("window.__afsPicked && window.__afsPicked(false)", null);
                    }
                }
            });
        }

        @JavascriptInterface public String list(String sub) {
            try {
                if (!permitted()) return null;
                String id = dirId(sub, false);
                return id == null ? "[]" : children(id).toString();
            } catch (Exception e) { Log.e(TAG, "list", e); return null; }
        }

        @JavascriptInterface public String stat(String sub, String name) {
            try {
                String id = dirId(sub, false);
                if (id == null) return null;
                JSONObject o = find(id, name);
                return o == null ? null : o.toString();
            } catch (Exception e) { return null; }
        }

        @JavascriptInterface public String read(String sub, String name) {
            try {
                String id = dirId(sub, false);
                if (id == null) return null;
                JSONObject o = find(id, name);
                if (o == null) return null;
                InputStream is = getContentResolver().openInputStream(docUri(o.getString("id")));
                if (is == null) return null;
                try {
                    ByteArrayOutputStream bo = new ByteArrayOutputStream();
                    byte[] buf = new byte[65536]; int n;
                    while ((n = is.read(buf)) > 0) bo.write(buf, 0, n);
                    return new String(bo.toByteArray(), StandardCharsets.UTF_8);
                } finally { is.close(); }
            } catch (Exception e) { Log.e(TAG, "read " + name, e); return null; }
        }

        @JavascriptInterface public boolean write(String sub, String name, String text) {
            return writeBytes(sub, name, text.getBytes(StandardCharsets.UTF_8));
        }

        @JavascriptInterface public boolean writeBase64(String sub, String name, String b64) {
            try { return writeBytes(sub, name, Base64.decode(b64, Base64.DEFAULT)); } catch (Exception e) { return false; }
        }

        @JavascriptInterface public boolean ensureDir(String sub) {
            try { return dirId(sub, true) != null; } catch (Exception e) { return false; }
        }

        @JavascriptInterface public boolean remove(String sub, String name) {
            try {
                String id = dirId(sub, false);
                if (id == null) return false;
                JSONObject o = find(id, name);
                return o != null && DocumentsContract.deleteDocument(getContentResolver(), docUri(o.getString("id")));
            } catch (Exception e) { return false; }
        }

        @JavascriptInterface public void toast(final String msg) {
            runOnUiThread(new Runnable() { @Override public void run() { Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show(); } });
        }
    }
}
