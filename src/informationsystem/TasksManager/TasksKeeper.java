package informationsystem.TasksManager;

import informationsystem.XmlReader;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TasksKeeper {
    static String PathToTests = ".\\pylint\\tests\\";

    private HashSet<TaskInfo> allTasks = new HashSet<>();
    private TaskInfo selectedTask;

    public TasksKeeper() {

    }

    public static TasksKeeper update(XmlReader reader) {
        return reader.getAlltests();
    }

    public void put(TaskInfo testData) {
        allTasks.add(testData);
    }

    public HashMap<String, String> getOldStyleTasks() {
        HashMap<String, String> oldStyleTasks = new HashMap<>();
        for (TaskInfo taskInfo : allTasks) {
            oldStyleTasks.put(taskInfo.getTaskName(), taskInfo.getTaskPath());
        }
        return oldStyleTasks;
    }

    public List<String> getAllTaskNames() {
        return allTasks.stream()
                .flatMap(p -> Stream.of(p.getTaskName()))
                .sorted()
                .collect(Collectors.toList());
    }

    public List<String> getAllTests(String taskName) throws IOException {
        TaskInfo taskInfo = getTestByName(taskName);
        setSelectedTask(taskInfo);
        List<String> tests = Files.list(Path.of(TasksKeeper.PathToTests, taskInfo.getTaskPath()))
                .filter(path -> path.toString().toLowerCase().endsWith(".t"))
                .flatMap(p -> Stream.of(p.getFileName().toString()))
                .collect(Collectors.toList());
        taskInfo.setTests(tests);

        return tests;
    }

    public TaskInfo getSelectedTask() {
        return selectedTask;
    }

    public void setSelectedTask(TaskInfo task) {
        this.selectedTask = task;
    }

    public TaskInfo getTestByName(String value) {
        return allTasks.stream().filter(item -> item.getTaskName().equals(value))
                .findFirst().get();
    }
}
