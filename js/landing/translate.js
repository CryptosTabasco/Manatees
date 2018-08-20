(function () {
    $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en'});
})();
$(document).ready(function () {

    $("#pt-br").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "pt-br", asyncLangLoad: false});
        })();
    });

    $("#italian").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "it", asyncLangLoad: false});
        })();
    });

    $("#french").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "fr", asyncLangLoad: false});
        })();
    });

    $("#german").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "de", asyncLangLoad: false});
        })();
    });

    $("#japanese").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "ja", asyncLangLoad: false});
        })();
    });

    $("#korean").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "kr", asyncLangLoad: false});
        })();
    });

    $("#chineese").on("click", function (e) {

        (function () {
            $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: "zh", asyncLangLoad: false});
        })();
    });

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
