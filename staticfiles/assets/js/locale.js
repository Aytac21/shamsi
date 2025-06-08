document.addEventListener("DOMContentLoaded", function () {
  console.log("Language switcher loaded");

  const languageSelector = document.getElementById("languageSelector");
  const currentLang = document.getElementById("currentLang");
  const currentLangText = document.getElementById("currentLangText");
  const dropdown = document.getElementById("dropdown");
  const langOptions = document.querySelectorAll(".lang-option");

  if (currentLang) {
    currentLang.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      console.log("Language selector clicked");
      languageSelector.classList.toggle("open");
    });
  }

  document.addEventListener("click", function () {
    if (languageSelector) {
      languageSelector.classList.remove("open");
    }
  });

  if (dropdown) {
    dropdown.addEventListener("click", function (e) {
      e.stopPropagation();
    });
  }

  langOptions.forEach((option) => {
    option.addEventListener("click", function (e) {
      e.preventDefault();
      console.log("Language option clicked");

      const selectedLang = this.getAttribute("data-lang");
      console.log("Selected language:", selectedLang);

      langOptions.forEach((opt) => opt.classList.remove("active"));
      this.classList.add("active");

      languageSelector.classList.remove("open");

      switchLanguage(selectedLang);
    });
  });

  function getCurrentLanguage() {
    const currentPath = window.location.pathname;
    if (currentPath.startsWith("/az/") || currentPath === "/az") {
      return "az";
    } else if (currentPath.startsWith("/ru/") || currentPath === "/ru") {
      return "ru";
    }
    return "en"; // default
  }

  function switchLanguage(langCode) {
    console.log("Switching to language:", langCode);

    localStorage.setItem("selected_language", langCode);

    let csrfValue = null;

    const csrfMeta = document.querySelector('meta[name="csrf-token"]');
    if (csrfMeta) {
      csrfValue = csrfMeta.getAttribute("content");
    }

    if (!csrfValue) {
      const csrfTokenInput = document.querySelector(
        'input[name="csrfmiddlewaretoken"]'
      );
      if (csrfTokenInput) {
        csrfValue = csrfTokenInput.value;
      }
    }

    if (!csrfValue) {
      const cookies = document.cookie.split(";");
      for (let cookie of cookies) {
        const [name, value] = cookie.trim().split("=");
        if (name === "csrftoken") {
          csrfValue = value;
          break;
        }
      }
    }

    console.log("CSRF token found:", csrfValue ? "Yes" : "No");

    const currentPath = window.location.pathname;
    const currentSearch = window.location.search;
    let newPath = currentPath;

    if (currentPath.startsWith("/az/")) {
      newPath = currentPath.substring(3);
    } else if (currentPath.startsWith("/en/")) {
      newPath = currentPath.substring(3);
    } else if (currentPath.startsWith("/ru/")) {
      newPath = currentPath.substring(3);
    } else if (
      currentPath === "/az" ||
      currentPath === "/en" ||
      currentPath === "/ru"
    ) {
      newPath = "/";
    }

    if (langCode === "az") {
      newPath = `/az${newPath === "/" ? "" : newPath}`;
    } else if (langCode === "ru") {
      newPath = `/ru${newPath === "/" ? "" : newPath}`;
    } else {
      newPath = newPath === "" ? "/" : newPath;
    }

    if (currentSearch) {
      newPath += currentSearch;
    }

    console.log("New path:", newPath);

    if (csrfValue) {
      const form = document.createElement("form");
      form.method = "POST";
      form.action = "/i18n/setlang/";
      form.style.display = "none";

      const csrfInput = document.createElement("input");
      csrfInput.type = "hidden";
      csrfInput.name = "csrfmiddlewaretoken";
      csrfInput.value = csrfValue;
      form.appendChild(csrfInput);

      const langInput = document.createElement("input");
      langInput.type = "hidden";
      langInput.name = "language";
      langInput.value = langCode;
      form.appendChild(langInput);

      const nextInput = document.createElement("input");
      nextInput.type = "hidden";
      nextInput.name = "next";
      nextInput.value = newPath;
      form.appendChild(nextInput);

      document.body.appendChild(form);
      form.submit();
    } else {
      console.warn("CSRF token not found, using simple redirect");
      window.location.href = newPath;
    }
  }

  function setActiveLanguageButton() {
    const savedLang = localStorage.getItem("selected_language");
    const currentPath = window.location.pathname;
    let currentLang = "en"; // default

    if (currentPath.startsWith("/az/") || currentPath === "/az") {
      currentLang = "az";
    } else if (currentPath.startsWith("/ru/") || currentPath === "/ru") {
      currentLang = "ru";
    } else if (savedLang && ["az", "en", "ru"].includes(savedLang)) {
      // URL'de dil belirtilmemişse ama localStorage'da varsa
      currentLang = savedLang;
    }

    if (currentLangText) {
      currentLangText.textContent = currentLang.toUpperCase();
    }

    langOptions.forEach((opt) => {
      opt.classList.remove("active");
    });

    const activeOption = document.querySelector(
      `.lang-option[data-lang="${currentLang}"]`
    );
    if (activeOption) {
      activeOption.classList.add("active");
    }

    localStorage.setItem("selected_language", currentLang);
  }

  if (currentLang) {
    currentLang.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        languageSelector.classList.toggle("open");
      }
    });
  }

  langOptions.forEach((option) => {
    option.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        option.click();
      }
    });
  });

  function updateNavLinks() {
    const savedLang =
      localStorage.getItem("selected_language") || getCurrentLanguage();
    const navLinks = document.querySelectorAll(
      ".navbar-nav .nav-link:not(.lang-option)"
    );

    navLinks.forEach((link) => {
      const href = link.getAttribute("href");
      if (href) {
        let newHref = href;

        newHref = newHref.replace(/^\/(az|en|ru)\//, "/");
        newHref = newHref.replace(/^\/(az|en|ru)$/, "/");

        if (savedLang === "az") {
          newHref = "/az" + (newHref === "/" ? "" : newHref);
        } else if (savedLang === "ru") {
          newHref = "/ru" + (newHref === "/" ? "" : newHref);
        } else {
          newHref = newHref === "" ? "/" : newHref;
        }

        link.setAttribute("href", newHref);
      }
    });
  }

  updateNavLinks();

  setActiveLanguageButton();

  let currentUrl = window.location.href;
  setInterval(() => {
    if (window.location.href !== currentUrl) {
      currentUrl = window.location.href;
      setActiveLanguageButton();
      updateNavLinks();
    }
  }, 100);
});
