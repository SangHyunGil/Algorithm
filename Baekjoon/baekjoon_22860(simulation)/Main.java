import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static class Folder {
        String name;
        List<Folder> folders = new ArrayList<>();
        List<File> files = new ArrayList<>();

        public Folder(String name) {
            this.name = name;
        }

        public void addFolder(Folder folder) {
            folders.add(folder);
        }

        public void addFile(File file) {
            files.add(file);
        }

        public List<Folder> getFolders() {
            return folders;
        }

        public List<File> getFiles() {
            return files;
        }
    }

    static class File {
        String name;

        public File(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<String, Folder> folderMap = new HashMap<>();

        for (int i = 0; i < n+m; i++) {
            st = new StringTokenizer(br.readLine());

            String upper = st.nextToken();
            String lower = st.nextToken();
            int type = Integer.parseInt(st.nextToken());

            if (!folderMap.containsKey(upper)) {
                folderMap.put(upper, new Folder(upper));
            }

            if (type == 1) {
                if (!folderMap.containsKey(lower)) {
                    folderMap.put(lower, new Folder(lower));
                }

                Folder upperFolder = folderMap.get(upper);
                upperFolder.addFolder(folderMap.get(lower));
            } else {
                Folder upperFolder = folderMap.get(upper);
                upperFolder.addFile(new File(lower));
            }
        }

        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            String[] folderName = br.readLine().split("/");
            String lastFolder = folderName[folderName.length - 1];
            Folder folder = folderMap.get(lastFolder);
            Map<String, Integer> files = new HashMap<>();
            solve(files, folder);
            System.out.println(files.size() + " " + files.values().stream().mapToInt(Integer::intValue).sum());
        }
    }

    private static void solve(Map<String, Integer> files, Folder folder) {
        for (File file : folder.getFiles()) {
            files.put(file.getName(), files.getOrDefault(file.getName(), 0)+1);
        }

        for (Folder innerFolder : folder.getFolders()) {
            solve(files, innerFolder);
        }
    }
}