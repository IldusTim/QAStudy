package com.easyqa.qa.pages;

import com.codeborne.selenide.Condition;
import org.openqa.selenium.support.FindBy;
import com.codeborne.selenide.SelenideElement;

import static com.codeborne.selenide.Selenide.page;

public class ProjectsPage {
    @FindBy(xpath = "//h1[.='My Projects']")
    public SelenideElement projectsHeader;

    @FindBy(xpath = "//div[@class='name-block']")
    public SelenideElement projectName;

    public void checkProjectsPage(){
        projectsHeader.shouldBe(Condition.visible);
    }

    public ProjectDashboardPage openProject(){
        projectName.click();
        return page(ProjectDashboardPage.class);
    }
}
