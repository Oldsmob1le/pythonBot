var WebApp = window.Telegram.WebApp;

WebApp.showAlert(`Добро пожаловать, @${WebApp.initDataUnsafe.user.username}.`);

var MainButton = WebApp.MainButton;
var BackButton = WebApp.BackButton;

MainButton.show();
BackButton.show();

MainButton.onClick(function () {
  WebApp.showAlert("Хорошо, ты нажал на главную кнопку.");
});
WebApp.onEvent("mainButtonClicked", function () {
  // Дополнительные действия при нажатии на главную кнопку
});

BackButton.onClick(function () {
  WebApp.showAlert("Нет пути назад!");
  BackButton.hide();
});
WebApp.onEvent("backButtonClicked", function () {
  // Дополнительные действия при нажатии на кнопку назад
});

// Пример отправки запроса на сервер
let xhrURL = new URL("https://<your_domain>/<createInvoiceLink>");
xhrURL.searchParams.set("title", "Example Title");
// Установите другие параметры

let xhr = new XMLHttpRequest();
xhr.open("GET", xhrURL);
xhr.send();
xhr.onload = function () {
  WebApp.openInvoice(JSON.parse(xhr.response).result);
};

WebApp.onEvent("invoiceClosed", function (object) {
  if (object.status == "paid") {
    WebApp.close();
  } else if (object.status == "failed") {
    WebApp.showAlert("Не беспокойтесь. Мы сохраним ваш выбор.");
  }
});

// Пример проверки данных пользователя
let initDataURLSP = new URLSearchParams(WebApp.initData);
var hash = initDataURLSP.get("hash");

initDataURLSP.delete("hash");
initDataURLSP.sort();
var checkDataString = initDataURLSP.toString().replaceAll("&", "\n");

let xhrURLCheck = new URL("https://<your_domain>/<userIsValid>");
xhrURLCheck.searchParams.set("hash", hash);
xhrURLCheck.searchParams.set("checkDataString", checkDataString);

let xhrCheck = new XMLHttpRequest();
xhrCheck.open("GET", xhrURLCheck);
xhrCheck.send();
xhrCheck.onload = function () {
  if (JSON.parse(xhrCheck.response).result == true) {
    WebApp.showAlert(`Добро пожаловать, @${WebApp.WebAppUser.username}.`);
  } else {
    WebApp.showAlert("Ты что, хакер?");
    WebApp.close();
  }
};
