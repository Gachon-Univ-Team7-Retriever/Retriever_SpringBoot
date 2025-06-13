package com.team7.retriever.util;

import java.util.regex.Pattern;

public class RegexUtils {
    public static String escape(String input) {
        return Pattern.quote(input);
    }
}
