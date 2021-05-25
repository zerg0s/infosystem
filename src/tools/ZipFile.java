package tools;

import lintsForLangs.MyPylint;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class ZipFile {
    public boolean unzipFileToDir(String fileZip, File destDir) {
        String dest1 = destDir.getAbsolutePath();
        boolean b1 = Files.exists(Paths.get(dest1));
        boolean b = Files.exists(Paths.get(fileZip));

        boolean result = true;
        byte[] buffer = new byte[1024];
        ZipInputStream zis = null;
        try {
            zis = new ZipInputStream(new FileInputStream(fileZip));

            ZipEntry zipEntry = zis.getNextEntry();
            while (zipEntry != null) {
                File newFile = newFile(destDir, zipEntry);
                if (!zipEntry.isDirectory()) {
                    FileOutputStream fos = new FileOutputStream(newFile);

                    int len;
                    while ((len = zis.read(buffer)) > 0) {
                        fos.write(buffer, 0, len);
                    }
                    fos.close();
                }
                zipEntry = zis.getNextEntry();
            }
            zis.closeEntry();
            zis.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            result = false;
        } catch (IOException e) {
            e.printStackTrace();
            result = false;
        }
        return result;
    }

    public String getPackageName(File javaFileFromArchive) {
        final String maiPackage = "package ";
        StringBuilder sb = new StringBuilder();
        try {
            List<String> linesOfFile = Files.readAllLines(javaFileFromArchive.toPath());
            for (String line : linesOfFile) {
                line = line.trim();
                if (line.trim().startsWith("package ")) {
                    String packageStr = line.substring(line.indexOf(' ') + 1, line.indexOf(';'));
                    return packageStr;
                }
            }
        } catch (IOException ex) {
            Logger.getLogger(MyPylint.class.getName()).log(Level.SEVERE, null, ex);
        }
        return "";
    }

    private File newFile(File destinationDir, ZipEntry zipEntry) throws IOException {
        File destFile = new File(destinationDir, zipEntry.getName());

        String destDirPath = destinationDir.getCanonicalPath();
        String destFilePath = destFile.getCanonicalPath();

        if (!destFilePath.startsWith(destDirPath + File.separator)) {
            throw new IOException("Entry is outside of the target dir: " + zipEntry.getName());
        }
        Path fileOrDirPath = destFile.toPath();
        Path parentalDirPath = new File(destFile.getParent()).toPath();

        if (!Files.exists(parentalDirPath)) {
            Files.createDirectories(parentalDirPath);
        }
        return destFile;
    }
}