/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import java.io.File;
import java.io.IOException;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import data.Project;
import data.ProjectOwner;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

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

import org.w3c.dom.Node;

/**
 * @author Zerg0s
 */
public class XmlReader {

    private String userName = "";
    private String apiKey = "";
    private String projectKey = "";
    private ArrayList<String> usersNameList = new ArrayList<String>();
    private ArrayList<String> apiKeysList = new ArrayList<String>();
    private ArrayList<String>  projectNameList = new ArrayList<String>();
    private ArrayList<ProjectOwner> owners = new ArrayList<ProjectOwner>();
    private String filePath = "";
    private boolean isEasyMode;
    private boolean checkAll;

    private String selectedSupervisor = "";
    private Project selectedProject;
    private String selectedVersion = "";

    public XmlReader(String pathToXml) {
        this.filePath = pathToXml;
    }

    XmlReader() {

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

    public void readXML(String filePath) {
        try {

            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setIgnoringElementContentWhitespace(true);
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(filePath);
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();

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

        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException ex) {
            Logger.getLogger(XmlReader.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            Logger.getLogger(XmlReader.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void saveSettings(String xmlPath, Map<String, String> settingsToSave) {
        XPathFactory xPathfactory = XPathFactory.newInstance();
        XPath xpath = xPathfactory.newXPath();

        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setIgnoringElementContentWhitespace(true);
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(xmlPath);
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
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File(xmlPath));
            //transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
            transformer.transform(source, result);

        } catch (ParserConfigurationException | SAXException | IOException | TransformerException e) {
            e.printStackTrace();
        }
    }

    public String getTestFolderBySubject(String subjectFromIssue) {
        String testFolderPathInXml = "";
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(this.filePath);
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();
            //xpath for gettings names
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
            Logger.getLogger(XmlReader.class.getName()).log(Level.SEVERE, null, ex);
        }
        return testFolderPathInXml;
    }

    public static String getValue(String tag, Element element) {
        NodeList nodes = element.getElementsByTagName(tag).item(0).getChildNodes();
        Node node = (Node) nodes.item(0);
        return node.getNodeValue();
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

    public HashMap<String, String> getAlltests() {
        HashMap<String, String> testsData = new HashMap<>();
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(this.filePath);
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();
            //xpath for settings names
            XPathExpression subjectFromXml = xpath.compile(".//test");
            NodeList listOfTestNodes = (NodeList) subjectFromXml.evaluate(doc, XPathConstants.NODESET);

            //тут можно добавить более "умный" поиск, пока ищем только - полное совпадение
            for (int i = 0; i < listOfTestNodes.getLength(); i++) {
                Element e = (Element) listOfTestNodes.item(i);
                testsData.put(e.getAttribute("subject"), e.getAttribute("testSetFolder"));
            }
        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException ex) {
            Logger.getLogger(XmlReader.class.getName()).log(Level.SEVERE, null, ex);
        }
        return testsData;
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
}
