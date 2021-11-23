package tools;

import informationsystem.loggerWindow.LoggerWindowController;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.logging.*;

public class PvkLogger {

    private ByteArrayOutputStream logStream;
    private StreamHandler streamHandler;
    private Logger logger;
    private static PvkLogger pvkLogger;
    private LoggerWindowController loggerWindow;

    protected PvkLogger(String name, boolean needConsole) {
        logger = Logger.getLogger(name);
        if (!needConsole) {
            Handler[] handlers = logger.getParent().getHandlers();
            if ((handlers.length > 0) && (handlers[0] instanceof ConsoleHandler)) {
                logger.getParent().removeHandler(handlers[0]);
            }
            logStream = new ByteArrayOutputStream();
            PrintStream prStr = new PrintStream(logStream);
            streamHandler = new StreamHandler(prStr, new SimpleFormatter());
            logger.addHandler(streamHandler);
        }
    }

    public void setLoggerControllerWindow(LoggerWindowController window) {
        this.loggerWindow = window;
    }

    public static PvkLogger getLogger(String name, boolean needConsole) {
        if (pvkLogger == null) {
            return new PvkLogger(name, needConsole);
        }
        return pvkLogger;
    }

    public static PvkLogger getLogger(String name) {
        if (pvkLogger == null) {
            return new PvkLogger(name, false);
        }
        return pvkLogger;
    }

    public void info(String data) {
        logger.info(data);
        flushAll(data);
    }

    public void warning(String data) {
        logger.info(data);
        flushAll(data);
    }

    public void error(String data) {
        logger.severe(data);
        flushAll(data);
    }

    private void flushAll(String data) {
        if (loggerWindow != null) {
            loggerWindow.appendLogs(data);
        }
        streamHandler.flush();
    }
}
