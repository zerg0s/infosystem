/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.OpenOption;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.xml.crypto.dsig.keyinfo.KeyValue;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import data.LintReportMode;
import data.Project;
import data.ProjectOwner;
import informationsystem.TasksManager.TaskInfo;
import informationsystem.TasksManager.TasksKeeper;
import javafx.util.Pair;
import org.w3c.dom.*;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import tools.TextUtils;
import tools.Translit;

import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

/**
 * @author Zerg0s
 */
public class XmlReader {

    private String userName = "";
    private String apiKey = "";
    private String projectKey = "";
    private ArrayList<String> usersNameList = new ArrayList<String>();
    private ArrayList<String> apiKeysList = new ArrayList<String>();
    private ArrayList<String> projectNameList = new ArrayList<String>();
    private ArrayList<ProjectOwner> owners = new ArrayList<ProjectOwner>();
    private String filePath = "";
    private boolean isEasyMode;
    private boolean checkAll;

    private String selectedSupervisor = "";
    private Project selectedProject;
    private String selectedVersion = "";

    private LintReportMode selectedLintMode;
    private XPathFactory xPathfactory = XPathFactory.newInstance();
    private XPath xpath = xPathfactory.newXPath();

    public XmlReader(String pathToXml) {
        this();
        this.filePath = pathToXml;
    }

    public XmlReader() {
        xPathfactory = XPathFactory.newInstance();
        xpath = xPathfactory.newXPath();
    }

    public void setUserName(String name) {
        this.userName = name;
    }

    public void setApiKey(String apikey) {
        this.apiKey = apikey;
    }

    public void setProjectKey(String projectkey) {
        this.projectKey = projectkey;
    }

    public void readConfigXML(String filePath) {
        try {
            Document doc = getDocument(filePath);

            //xpath for gettings names
            XPathExpression exprOwners = xpath.compile(".//supervisor/@name");
            NodeList nl = (NodeList) exprOwners.evaluate(doc, XPathConstants.NODESET);
            for (int i = 0; i < nl.getLength(); i++) {
                String owner = nl.item(i).getTextContent();
                getOwners().add(new ProjectOwner(owner));
                //get all project by supervisor
                XPathExpression exprProjects = xpath.compile(".//supervisor[@name='" + owner + "']/project");
                NodeList hisProjects = (NodeList) exprProjects.evaluate(doc, XPathConstants.NODESET);
                for (int j = 0; j < hisProjects.getLength(); j++) {
                    Element e = (Element) hisProjects.item(j);
                    String name = e.getAttribute("name");
                    String id = e.getAttribute("id");
                    getOwners().get(i).getHisProjects().add(new Project(name, id));
                }
                //add apikey
                XPathExpression exprApiKey = xpath.compile(".//supervisor[@name='" + owner + "']/apiKey");
                NodeList hisApikey = (NodeList) exprApiKey.evaluate(doc, XPathConstants.NODESET);
                getOwners().get(i).setApiKey(hisApikey.item(0).getTextContent());
            }
            XPathExpression isEasyModeXpath = xpath.compile(".//isEasyMode");
            Node easyModeNode = (Node) isEasyModeXpath.evaluate(doc, XPathConstants.NODE);
            if (easyModeNode != null) {
                isEasyMode = Boolean.parseBoolean(easyModeNode.getTextContent());
            }

            XPathExpression isCheckAllXpath = xpath.compile(".//checkAllIterations");
            Node isCheckAllNode = (Node) isCheckAllXpath.evaluate(doc, XPathConstants.NODE);
            if (isCheckAllNode != null) {
                checkAll = Boolean.parseBoolean(isCheckAllNode.getTextContent());
            }

            XPathExpression selectedSupervisorXpath = xpath.compile(".//SelectedSupervisor");
            Node selectedSupervisorNode = (Node) selectedSupervisorXpath.evaluate(doc, XPathConstants.NODE);
            if (selectedSupervisorNode != null) {
                selectedSupervisor = selectedSupervisorNode.getTextContent();
            }

            XPathExpression selectedProjectXPath = xpath.compile(".//SelectedProjectName");
            XPathExpression selectedProjectIdXPath = xpath.compile(".//SelectedProjectId");
            Node selectedProjectNode = (Node) selectedProjectXPath.evaluate(doc, XPathConstants.NODE);
            Node selectedProjectIdNode = (Node) selectedProjectIdXPath.evaluate(doc, XPathConstants.NODE);
            if (selectedProjectNode != null && selectedProjectNode != null) {
                selectedProject = new Project(selectedProjectNode.getTextContent(), selectedProjectIdNode.getTextContent());
            }

            Node selectedVersionNode = (Node) xpath.compile(".//SelectedIteration").evaluate(doc, XPathConstants.NODE);
            if (selectedVersionNode != null) {
                selectedVersion = selectedVersionNode.getTextContent();
            }

            XPathExpression selectedLintModeXpath = xpath.compile(".//SelectedLintMode");
            Node selectedLintModeNode = (Node) selectedLintModeXpath.evaluate(doc, XPathConstants.NODE);
            if (selectedLintModeNode != null) {
                selectedLintMode = LintReportMode.valueOf(selectedLintModeNode.getTextContent());
            }

        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException ex) {
            logger.info(ex.getMessage());
        } catch (Exception ex) {
            logger.info(ex.getMessage());
        }
    }

    public void saveSettings(String xmlPath, Map<String, String> settingsToSave) {
        try {
            Document doc = getDocument(xmlPath);
            Element settingsNode = doc.getDocumentElement();
            settingsNode.normalize();
            for (Map.Entry m : settingsToSave.entrySet()) {
                if (settingsNode.getElementsByTagName((String) m.getKey()).getLength() == 0) {
                    Element aSetting = doc.createElement((String) m.getKey());
                    aSetting.appendChild(doc.createTextNode((String) m.getValue()));
                    settingsNode.appendChild(aSetting);
                } else {
                    Node el = settingsNode.getElementsByTagName((String) m.getKey()).item(0);
                    el.setTextContent((String) m.getValue());
                }
            }
            //save xml
            saveXml(doc, xmlPath);

        } catch (ParserConfigurationException | SAXException | IOException | TransformerException e) {
            e.printStackTrace();
        }
    }

    public String getTestFolderBySubject(String subjectFromIssue) {
        String testFolderPathInXml = "";
        try {
            Document doc = getDocument(filePath);
            //xpath for getting names
            XPathExpression subjectFromXml = xpath.compile(".//test");
            NodeList listOfTestNodes = (NodeList) subjectFromXml.evaluate(doc, XPathConstants.NODESET);

            //тут можно добавить более "умный" поиск, пока ищем только - полное совпадение
            for (int i = 0; i < listOfTestNodes.getLength(); i++) {
                Element e = (Element) listOfTestNodes.item(i);
                if (subjectFromIssue.toLowerCase().contains(e.getAttribute("subject").toLowerCase())) {
                    testFolderPathInXml = e.getAttribute("testSetFolder");
                }
            }
        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException ex) {
            logger.info(ex.getMessage());
        }
        return testFolderPathInXml;
    }

    public LintReportMode getSelectedLintMode() {
        return selectedLintMode;
    }

    /**
     * @return the userName
     */
    public String getUserName() {
        return userName;
    }

    /**
     * @return the apiKey
     */
    public String getApiKey() {
        return apiKey;
    }

    /**
     * @return the projectKey
     */
    public String getProjectKey() {
        return projectKey;
    }

    /**
     * @return the usersNameList
     */
    public ArrayList<String> getUsersNameList() {
        return usersNameList;
    }

    /**
     * @param usersNameList the usersNameList to set
     */
    public void setUsersNameList(ArrayList<String> usersNameList) {
        this.usersNameList = usersNameList;
    }

    /**
     * @return the projectNameList
     */
    public ArrayList<String> getProjectNameList(String ownerName) {
        projectNameList.clear();
        for (ProjectOwner owner : this.owners) {
            if (owner.getName().equals(ownerName)) {
                for (Project project : owner.getHisProjects()) {
                    projectNameList.add(project.getProjectName());
                }
            }
        }
        return projectNameList;
    }

    public String getSelectedSupervisor() {
        return selectedSupervisor;
    }

    /**
     * @param projectNameList the projectNameList to set
     */
    public void setProjectNameList(ArrayList<String> projectNameList) {
        this.projectNameList = projectNameList;
    }

    /**
     * @return the apiKeysList
     */
    public ArrayList<String> getApiKeysList() {
        return apiKeysList;
    }

    /**
     * @param apiKeysList the apiKeysList to set
     */
    public void setApiKeysList(ArrayList<String> apiKeysList) {
        this.apiKeysList = apiKeysList;
    }

    /**
     * @return the owners
     */
    public ArrayList<ProjectOwner> getOwners() {
        return owners;
    }

    /**
     * @param owners the owners to set
     */
    public void setOwners(ArrayList<ProjectOwner> owners) {
        this.owners = owners;
    }

    public TasksKeeper getAllTests() {
        //HashMap<String, String> testsData = new HashMap<>();
        TaskInfo testData;
        TasksKeeper tasksKeeper = new TasksKeeper();

        try {
            Document doc = getDocument(filePath);
            //xpath for settings names
            XPathExpression subjectFromXml = xpath.compile(".//test");
            NodeList listOfTestNodes = (NodeList) subjectFromXml.evaluate(doc, XPathConstants.NODESET);

            //тут можно добавить более "умный" поиск, пока ищем только - полное совпадение
            for (int i = 0; i < listOfTestNodes.getLength(); i++) {
                testData = new TaskInfo();
                Element e = (Element) listOfTestNodes.item(i);
                testData.setTaskName(e.getAttribute("subject"));
                testData.setTaskPath(e.getAttribute("testSetFolder"));
                testData.setTaskId(e.getAttribute("id"));
                NodeList listOfDescr = e.getChildNodes();
                for (int j = 0; j < listOfDescr.getLength(); j++) {
                    Node node = (Node) listOfDescr.item(j);
                    if (node.getNodeName().equals("description")) {
                        testData.setTaskBody(node.getTextContent().trim());
                    }
                }
                tasksKeeper.put(testData);
            }
        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException ex) {
            logger.info(ex.getMessage());
        }

        return tasksKeeper;
    }

    public boolean isEasyMode() {
        return isEasyMode;
    }

    public boolean needCheckAllIterations() {
        return checkAll;
    }

    public Project getSelectedProject() {
        return selectedProject;
    }

    public String getSelectedVersion() {
        return selectedVersion;
    }

    public void addIteration(String iterationName) {
        try {
            Document doc = getDocument(filePath);
            Element rootNode = doc.getDocumentElement();
            rootNode.normalize();
            Node node = doc.createTextNode("homework");
            ((Element) node).setAttribute("id", Translit.toTranslit(iterationName));
            rootNode.appendChild(node);
            saveXml(doc, filePath);
        } catch (ParserConfigurationException | SAXException | IOException | TransformerException e) {
            e.printStackTrace();
        }
    }

    public void saveTask(TaskInfo selectedTask) {
        try {
            Document doc = getDocument(filePath);
            Element rootNode = doc.getDocumentElement();
            rootNode.normalize();

            Element foundElement = (Element) getTask(selectedTask);

            //may be it already has a description
            String xPathString = String.format("./description");
            Element description = (Element) xpath.evaluate(xPathString, foundElement, XPathConstants.NODE);

            if (description != null) {
                Node newNode = description.getFirstChild();
                if (newNode != null) {
                    newNode.setTextContent(selectedTask.getTaskBody());
                    description.replaceChild(description.getFirstChild(), newNode);
                } else {
                    description.appendChild(doc.createCDATASection(selectedTask.getTaskBody()));
                }
            } else {
                if (foundElement.getAttribute("subject").equalsIgnoreCase(selectedTask.getTaskName())) {
                    Element newDescription = doc.createElement("description");
                    CDATASection newDescriptionCdata = doc.createCDATASection(selectedTask.getTaskBody());
                    newDescription.appendChild(newDescriptionCdata);
                    foundElement.appendChild(newDescription);
                }
            }

            //set new subject
            foundElement.setAttribute("subject", selectedTask.getTaskName());
            saveXml(doc, filePath);

        } catch (ParserConfigurationException | SAXException | IOException | TransformerException | XPathExpressionException e) {
            e.printStackTrace();
        }
    }

    /// private methods
    private Node getTask(TaskInfo selectedTask) {
        Element foundElement = null;
        try {
            Document doc = getDocument(filePath);
            Element rootNode = doc.getDocumentElement();
            rootNode.normalize();

            //find the test Node
            String xPathStringElem = String.format(".//test[@id=\"%s\"]", selectedTask.getTaskId());
            foundElement = (Element) xpath.evaluate(xPathStringElem, rootNode, XPathConstants.NODE);
            if (foundElement == null) {
                xPathStringElem = String.format(".//test[@subject=\"%s\"]", selectedTask.getTaskName());
                foundElement = (Element) xpath.evaluate(xPathStringElem, rootNode, XPathConstants.NODE);
            }
            if (foundElement == null) {
                xPathStringElem = String.format(".//test[@subject=\"%s\"]", Translit.toTranslit(selectedTask.getTaskName()));
                foundElement = (Element) xpath.evaluate(xPathStringElem, rootNode, XPathConstants.NODE);
            }

        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException e) {
            e.printStackTrace();
        }
        return foundElement;
    }

    private Document getDocument(String filePath) throws ParserConfigurationException, SAXException, IOException {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setIgnoringElementContentWhitespace(true);
        DocumentBuilder builder = factory.newDocumentBuilder();
        return builder.parse(filePath);
    }

    private void saveXml(Document doc, String filePath) throws TransformerException {
        Transformer transformer = TransformerFactory.newInstance().newTransformer();
        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new File(filePath));
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");
        transformer.transform(source, result);
        //Crunch remove empty lines
        try {
            List<String> xmlString = Files.readAllLines(Path.of(filePath));
            Files.delete(Path.of(filePath));
            BufferedWriter wr = new BufferedWriter(new FileWriter(filePath, StandardCharsets.UTF_8));
            for (String s : xmlString) {
                if (s.trim().isEmpty()) {
                    continue;
                }
                wr.write(s);
                wr.newLine();
            }

            wr.flush();
            wr.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public boolean exists(TaskInfo task) {
        return getTask(task) != null;
    }


    public void addTask(TaskInfo selectedTask) {
        try {
            Document doc = getDocument(filePath);
            Element rootNode = doc.getDocumentElement();
            rootNode.normalize();

            Element nodeForAnewTask = (Element) chooseNodeForANewTask(selectedTask, xpath, doc, rootNode);

            Element taskNode = doc.createElement("test");
            String taskId = !TextUtils.isNullOrEmpty(selectedTask.getTaskId()) ? selectedTask.getTaskId() :
                    getNextId(rootNode);
            taskNode.setAttribute("id", taskId);
            taskNode.setAttribute("testSetFolder", selectedTask.getTaskPath());
            taskNode.setAttribute("subject", selectedTask.getTaskName());
            Element newDescription = doc.createElement("description");
            CDATASection newDescriptionCdata = doc.createCDATASection(selectedTask.getTaskBody());
            newDescription.appendChild(newDescriptionCdata);
            taskNode.appendChild(newDescription);
            nodeForAnewTask.appendChild(taskNode);
            saveXml(doc, filePath);
        } catch (ParserConfigurationException | SAXException | IOException | TransformerException | XPathExpressionException e) {
            logger.info(e.getMessage());
        }
    }

    private String getNextId(Element rootNode) {
        String xPathStringElem = ".//homework/test/@id";
        NodeList ids = null;
        try {
            ids =
                    (NodeList) xpath.evaluate(xPathStringElem, rootNode, XPathConstants.NODESET);
        } catch (XPathExpressionException ex) {
            logger.info(ex.getMessage());
        }
        int max = 0;
        for (int i = 0; i < ids.getLength(); i++) {
            if (Integer.parseInt(ids.item(i).getNodeValue()) > max) {
                max = Integer.parseInt(ids.item(i).getNodeValue());
            }
        }
        return String.valueOf(max + 1);
    }

    private Node chooseNodeForANewTask(TaskInfo selectedTask, XPath xpath, Document doc, Element rootNode) throws XPathExpressionException {
        Element pathforAnewTask = null;
        if (selectedTask.getIterationPath() != null || !selectedTask.getIterationPath().equals("")) {
            String xPathStringElem = String.format(".//homework[@name=\"%s\"]", selectedTask.getIterationPath());
            pathforAnewTask = (Element) xpath.evaluate(xPathStringElem, rootNode, XPathConstants.NODE);
            if (pathforAnewTask == null) {
                xPathStringElem = String.format(".//homework[@name=\"%s\"]", Translit.toTranslit(selectedTask.getIterationPath()));
                pathforAnewTask = (Element) xpath.evaluate(xPathStringElem, rootNode, XPathConstants.NODE);
            }

            if (pathforAnewTask == null) {
                pathforAnewTask = doc.createElement("homework");
                pathforAnewTask.setAttribute("name", selectedTask.getIterationPath());
                rootNode.appendChild(pathforAnewTask);
            }
        } else {
            String xPathStringElem = String.format(".//homework[@name=\"%s\"]", "");
            pathforAnewTask = (Element) xpath.evaluate(xPathStringElem, rootNode, XPathConstants.NODE);
            if (pathforAnewTask == null) {
                pathforAnewTask = doc.createElement("homework");
                pathforAnewTask.setAttribute("name", "");
                rootNode.appendChild(pathforAnewTask);
            }
        }
        return pathforAnewTask;
    }

    //// Static methods
    public static String getValue(String tag, Element element) {
        if (tag != null && element != null) {
            Node node = element.getElementsByTagName(tag).item(0);
            if (node != null) {
                Node childNode = node.getChildNodes().item(0);
                return childNode.getNodeValue();
            }
        }
        return "";
    }

    public static Document loadXMLFromString(String xml) throws ParserConfigurationException, IOException, SAXException {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        InputSource is = new InputSource(new StringReader(xml));
        return builder.parse(is);
    }

    public static String getTextTagValue(String tag, Document doc) {
        return getValue(tag, doc.getDocumentElement());
    }

    public static List<String> getDescription(String readXml, String descriptionTag, String itemTag) throws IOException, SAXException, ParserConfigurationException {
        NodeList nodes = loadXMLFromString(readXml).getDocumentElement()
                .getElementsByTagName(itemTag);
        List<String> nodesList = new ArrayList<>();
        for (int i = 0; i < nodes.getLength(); i++) {
            nodesList.add(((Node) nodes.item(i)).getChildNodes().item(0).getNodeValue());
        }
        return nodesList;
    }

    public static Pair<String, String> getFilePath(String xml, String attribute) {
        Pair<String, String> fromTo = new Pair<String, String>("", "");
        try {
            final Document doc = loadXMLFromString(xml);
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();

            //xpath for gettings paths
            String xPath = String.format(".//files/file[@descr=\"%s\"]", attribute);
            XPathExpression exprFrom = xpath.compile(xPath);
            Element fileNode = (Element) exprFrom.evaluate(doc, XPathConstants.NODE);
            fromTo = new Pair<String, String>(fileNode.getAttribute("from"),
                    fileNode.getAttribute("to"));
        } catch (ParserConfigurationException | IOException | SAXException | XPathExpressionException e) {
            e.printStackTrace();
        }
        return fromTo;
    }

    public static ArrayList<Pair<String, String>> getAllAdditionalFiles(String xml) {
        Pair<String, String> fromTo;
        ArrayList<Pair<String, String>> files = new ArrayList<>();
        try {
            final Document doc = loadXMLFromString(xml);
            NodeList fileNodes = ((Element) doc.getElementsByTagName("root").item(0)).getElementsByTagName("file");
            for (int i = 0; i < fileNodes.getLength(); i++) {
                Element fileElement = (Element) fileNodes.item(i);
                fromTo = new Pair<String, String>(fileElement.getAttribute("from"),
                        fileElement.getAttribute("to"));
                files.add(fromTo);
            }
        } catch (ParserConfigurationException | IOException | SAXException e) {
            e.printStackTrace();
        }
        return files;
    }

    private static Logger logger = Logger.getLogger(FXMLDocumentController.class.getSimpleName());
}
