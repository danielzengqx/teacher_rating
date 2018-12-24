/*!
 * Star Rating Chinese Translations
 *
 * This file must be loaded after 'star-rating.js'. Patterns in braces '{}', or
 * any HTML markup tags in the messages must not be converted or translated.
 *
 * NOTE: this file must be saved in UTF-8 encoding.
 *
 * @see http://github.com/kartik-v/bootstrap-star-rating
 * @author Kartik Visweswaran <kartikv2@gmail.com>
 * @author Freeman
 */
 (function ($) {
    "use strict";
    $.fn.ratingLocales['zh'] = {
        defaultCaption: '{rating} 分 ',
        starCaptions: {
            0.5: '半分',
            1: '一分',
            1.5: '一分半',
            2: '二分',
            2.5: '二分半',
            3: '三分',
            3.5: '三分半',
            4: '四分',
            4.5: '四分半',
            5: '五分',
            5.5: '五分半',
            6: '六分',
            6.5: '六分半',
            7: '七分',
            7.5: '七分半',
            8: '八分',
            8.5: '八分半',
            9: '九分',
            9.5: '九分半',
            10: '十分'

        },
        clearButtonTitle: '清除',
        clearCaption: '未评级'
    };
})(window.jQuery);
