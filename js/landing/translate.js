

function selectLanguage( language ) {
   $("[data-translate]").jqTranslate('i18n/index', {defaultLang: 'en', forceLang: language, asyncLangLoad: false});
}

$(document).ready(function ( ) {

    selectLanguage( 'en' );

    $(".lang-selector").on("click", function (e) {
        var language =  e.target.id;
        selectLanguage( language );
    });

});
