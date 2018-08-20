(function () {
    $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en'});
})();
$(document).ready(function () {

    $("#spanish").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "es", asyncLangLoad: false});
        })();
    });

    $("#english").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'es', forceLang: "en", asyncLangLoad: false});
        })();
    })

});