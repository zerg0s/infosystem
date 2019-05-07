/*
 * To change this license header, choose License Headers in Project RedmineConnectionProperties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package informationsystem;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;

/**
 *
 * @author user
 */
public class XmlReader {

    private String userName = "";
    private String apiKey = "";
    private String projectKey = "";
    private ArrayList<String> usersNameList = new ArrayList<String>();
    private ArrayList<String> projectIDsList = new ArrayList<String>();
    private ArrayList<String> projectNameList = new ArrayList<String>();
    private ArrayList<String> apiKeysList = new ArrayList<String>();
    private ArrayList<ProjectOwner> owners = new ArrayList<ProjectOwner>();
    private String filePath = "";

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
        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException ex) {
            Logger.getLogger(XmlReader.class.getName()).log(Level.SEVERE, null, ex);
        }

        //тут собрали Arraylist владельцев проектов с их проектами и ключами.
        getOwners().forEach((ProjectOwner p) -> {
            System.out.println(p);
        });

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

    private static String getValue(String tag, Element element) {
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
     * @return the projectIDsList
     */
    public ArrayList<String> getProjectIDsList() {
        return projectIDsList;
    }

    /**
     * @param projectIDsList the projectIDsList to set
     */
    public void setProjectIDsList(ArrayList<String> projectIDsList) {
        this.projectIDsList = projectIDsList;
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

    HashMap<String, String> getAlltests() {
        HashMap<String, String> testsData = new HashMap<>();
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
                testsData.put(e.getAttribute("subject"), e.getAttribute("testSetFolder"));
            }
        } catch (ParserConfigurationException | SAXException | IOException | XPathExpressionException ex) {
            Logger.getLogger(XmlReader.class.getName()).log(Level.SEVERE, null, ex);
        }
        return testsData;
    }
}
