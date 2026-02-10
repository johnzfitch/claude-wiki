<!-- Source: https://claude.com/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation -->

:root {
 --grid-breakout: [full-start] minmax(0, 1fr) [content-start] repeat(var(--_grid---column-count), minmax(0, var(--_grid---column-width))) [content-end] minmax(0, 1fr) [full-end];
 --grid-breakout-single: [full-start] minmax(0, 1fr) [content-start] minmax(0, calc(100% - var(--site--margin) * 2)) [content-end] minmax(0, 1fr) [full-end];
 }
 ::before, ::after {
 box-sizing: border-box;
 }
 .w-embed:before, .w-embed:after,
 .w-richtext:before, .w-richtext:after {
 content: unset;
 }
 html {
 background-color: var(--_theme---background);
 }
 button {
 background-color: unset;
 padding: unset;
 text-align: inherit;
 }
 button:not(:disabled) {
 cursor: pointer;
 }
 video {
 width: 100%;
 object-fit: cover;
 }
 /* remove padding of empty element */
 .wf-empty {
 padding: 0;
 }
 svg {
 max-width: 100%;
 }
 @media (prefers-color-scheme: light) {
 option { color: black; }
 }
 img::selection {
 background: transparent;
 }
 /* Typography */
 body {
 text-transform: var(--_text-style---text-transform);
 font-smoothing: antialiased;
 -webkit-font-smoothing: antialiased;
 }

 /* Clear Defaults */
 a:not ([class]) {
 text-decoration: underline;} 

 [class~="u-rich-text"] a,
 [class~="u-rich-text-cs"] a,
 [class~="u-rich-text-blog"] a,
 [class~="u-rich-text-tutorials"] a,
 a.u-rich-text,
 [class~="command_instruction"] a {
 transition: color .15s ease-out, text-decoration-color .15s ease-out;
 text-underline-offset: 3px;
 text-decoration: underline;
 color: currentcolor;
 text-decoration-color: var(--_theme---border-primary);
 }

 [class~="u-rich-text"] a:hover,
 [class~="u-rich-text-cs"] a:hover,
 [class~="u-rich-text-blog"] a:hover,
 [class~="u-rich-text-tutorials"] a:hover,
 a.u-rich-text:hover,
 [class~="command_instruction"] a:hover {
 text-decoration-color: var(--_theme---foreground-primary);
 color: var(--_theme---foreground-primary);
 }

 h1,h2,h3,h4,h5,h6,p,blockquote,label {
 font-family: inherit;
 font-size: inherit;
 font-weight: inherit;
 line-height: inherit;
 letter-spacing: inherit;
 text-transform: inherit;
 text-wrap: inherit;
 margin-top: 0;
 margin-bottom: 0;
 }
 select:has(option[value=""]:checked) {
 color: color-mix(in lab, currentcolor 60%, transparent)
 }
 /* Selection Color */
 ::selection {
 background-color: var(--_theme---selection--background);
 color: var(--_theme---selection--text);
 }
 /* Margin Trim */
 :is(.u-margin-trim,.u-rich-text) > :not(:not(.w-condition-invisible,.u-cover-absolute,.u-ignore-trim) ~ :not(.w-condition-invisible,.u-cover-absolute,.u-ignore-trim)),
 :is(.u-margin-trim,.u-rich-text) > :not(:not(.w-condition-invisible,.u-cover-absolute,.u-ignore-trim) ~ :not(.w-condition-invisible,.u-cover-absolute,.u-ignore-trim)).u-display-contents > :first-child {
 margin-top: 0;
 }
 :is(.u-margin-trim,.u-rich-text) > :not(:has(~ :not(.w-condition-invisible,.u-cover-absolute,.u-ignore-trim))),
 :is(.u-margin-trim,.u-rich-text) > :not(:has(~ :not(.w-condition-invisible,.u-cover-absolute,.u-ignore-trim))).u-display-contents > :last-child {
 margin-bottom: 0;
 }
 /* Line Height Trim */
 :is(h1,h2,h3,h4,h5,h6,p):not(.u-text-trim-off,:has([class*="u-text-style-"]))::before,
 [class*="u-text-style-"]:not(.u-text-trim-off,:has(h1,h2,h3,h4,h5,h6,p))::before {
 content: "";
 display: table;
 margin-bottom: calc(-0.5lh + var(--_text-style---trim-top));
 }
 :is(h1,h2,h3,h4,h5,h6,p):not(.u-text-trim-off,:has([class*="u-text-style-"]))::after,
 [class*="u-text-style-"]:not(.u-text-trim-off,:has(h1,h2,h3,h4,h5,h6,p))::after {
 content: "";
 display: table;
 margin-bottom: calc(-0.5lh + var(--_text-style---trim-bottom));
 }
 /* Rich Text Links */
 .w-richtext a {
 position: relative;
 z-index: 4;
 }
 /* Line Clamp */
 .u-line-clamp-1, .u-line-clamp-2, .u-line-clamp-3, .u-line-clamp-4 {
 -webkit-line-clamp: 1;
 -webkit-box-orient: vertical;
 }
 .u-line-clamp-2 { -webkit-line-clamp: 2; }
 .u-line-clamp-3 { -webkit-line-clamp: 3; }
 .u-line-clamp-4 { -webkit-line-clamp: 4; }
 /* Child Contain */
 .u-child-contain > * {
 width: 100%;
 max-width: inherit !important;
 margin-inline: 0 !important;
 margin-top: 0 !important;
 }
 /* Hide */
 .u-hide-if-empty:empty,
 .u-hide-if-empty:not(:has(> :not(.w-condition-invisible))),
 .u-hide-if-empty-cms:not(:has(.w-dyn-item)),
 .u-embed-js,
 .u-embed-css {
 display: none !important;
 }
 /* Focus State */
 a, button, :where([tabindex]), [data-outline] {
 outline-offset: var(--focus--offset-outer);
 }
 a:focus-visible,
 button:focus-visible,
 [tabindex]:focus-visible,
 label:has(input:focus-visible) [data-outline] {
 outline-color: color-mix(in srgb, var(--_button-style---border) 50%, transparent);
 outline-width: var(--focus--width);
 outline-style: solid;
 }

 /* Global / Clickable Component */
 .wf-design-mode .clickable_wrap {
 z-index: 0;
 }
 .clickable_wrap a[href="#"] {
 display: none;
 }
 .clickable_wrap a[href="#"] ~ button {
 display: block;
 }
 /* Responsive Above */
 @container threshold-large (width >= 62em) {
 .u-order-unset-above { order: unset !important; }
 .u-all-unset-above { all: unset !important; }
 .u-grid-below { display: flex !important; }
 .u-max-width-unset-above { max-width: unset !important; }
 .u-width-unset-above { width: unset !important; }
 .u-hide-above { display: none !important; }
 }
 @container threshold-medium (width >= 48em) {
 .u-order-unset-above { order: unset !important; }
 .u-all-unset-above { all: unset !important; }
 .u-grid-below { display: flex !important; }
 .u-max-width-unset-above { max-width: unset !important; }
 .u-width-unset-above { width: unset !important; }
 .u-hide-above { display: none !important; }
 }
 @container threshold-small (width >= 30em) {
 .u-order-unset-above { order: unset !important; }
 .u-all-unset-above { all: unset !important; }
 .u-grid-below { display: flex !important; }
 .u-max-width-unset-above { max-width: unset !important; }
 .u-width-unset-above { width: unset !important; }
 .u-hide-above { display: none !important; }
 }
 /* Responsive Below */
 @container threshold-large (width < 62em) {
 .u-order-unset-below { order: unset !important; }
 .u-all-unset-below { all: unset !important; }
 .u-grid-above { display: flex !important; }
 .u-max-width-unset-below { max-width: unset !important; }
 .u-width-unset-below { width: unset !important; }
 .u-alignment-unset-below {
 --_alignment---direction: start;
 align-self: start;
 }
 .u-hide-below { display: none !important; }
 }
 @container threshold-medium (width < 48em) {
 .u-order-unset-below { order: unset !important; }
 .u-all-unset-below { all: unset !important; }
 .u-grid-above { display: flex !important; }
 .u-max-width-unset-below { max-width: unset !important; }
 .u-width-unset-below { width: unset !important; }
 .u-alignment-unset-below {
 --_alignment---direction: start;
 align-self: start;
 }
 .u-hide-below { display: none !important; }
 }
 @container threshold-small (width < 30em) {
 .u-order-unset-below { order: unset !important; }
 .u-all-unset-below { all: unset !important; }
 .u-grid-above { display: flex !important; }
 .u-max-width-unset-below { max-width: unset !important; }
 .u-width-unset-below { width: unset !important; }
 .u-alignment-unset-below {
 --_alignment---direction: start;
 align-self: start;
 }
 .u-hide-below { display: none !important; }
 }
 /* Form Radio */
 .form_main_radio_label:has(input:checked) .form_main_radio_circle_inner {
 opacity: 1;
 }
 /* Form Checkbox */
 .form_main_checkbox_label:has(input:checked) .form_main_checkbox_box {
 background-color: currentColor;
 border-color: currentColor;
 }
 .form_main_checkbox_label:has(input:checked) .form_main_checkbox_icon {
 opacity: 1;
 }
 /* State Manager */
 [data-state] { --_state---true: 1; --_state---false: 0; }
 .is-active,
 [data-state~="checked"]:is(:checked, :has(:checked)),
 [data-state~="current"]:is(.w--current, :has(.w--current)),
 [data-state~="open"]:is(.w--open, :has(.w--open)),
 [data-state~="expanded"]:is([aria-expanded="true"], :has([aria-expanded="true"])),
 [data-state~="external"]:is([target="_blank"], :has([target="_blank"])) { 
 --_state---true: 0; --_state---false: 1;
 }
 .wf-design-mode [data-trigger~="preview"],
 [data-trigger~="focus"]:is(:focus-visible, :has(:focus-visible)),
 [data-trigger~="group"]:has([data-trigger~="focus-other"]:focus-visible, [data-trigger~="focus-other"] :focus-visible)
 [data-trigger~="focus-other"]:not(:focus-visible, :has(:focus-visible)) {
 --_trigger---on: 0; --_trigger---off: 1;
 }
 @media (hover: hover) {
 [data-button]:hover,
 [data-trigger~="hover"]:is(a:hover,button:hover,:has(a:hover,button:hover)),
 [data-trigger~="group"]:has([data-trigger~="hover-other"]:hover) [data-trigger~="hover-other"]:not(:hover) { 
 --_trigger---on: 0; --_trigger---off: 1;
 }
 [data-trigger~="hover-other"]:hover { --_trigger---on: 1 !important; --_trigger---off: 0 !important; }
 }
 @media (hover: none) {
 [data-trigger~="mobile"] { --_trigger---on: 0; --_trigger---off: 1; }
 }

 code, kbd, pre, samp {
 font-family: var(--_typography---font--mono-family);
 }
 body * {
 scrollbar-width: none; /* Firefox */
 -ms-overflow-style: none; /* IE/Edge Legacy */
 }
 body *::-webkit-scrollbar {
 display: none; /* Unreliable */
 width: 0px; /* WebKit/Blink */
 }

 @media (prefers-color-scheme: dark) {
 body,
 .u-theme-ivory,
 [data-wf--section--theme="ivory"] {
 --_theme---background-primary: var(--swatch--gray-950);
 --_theme---background-secondary: var(--swatch--gray-900);
 --_theme---background-tertiary: var(--swatch--gray-850);
 --_theme---border-primary: var(--swatch--gray-600);
 --_theme---border-secondary: var(--swatch--gray-700);
 --_theme---border-tertiary: var(--swatch--gray-750);
 --_theme---foreground-primary: var(--swatch--gray-050);
 --_theme---foreground-secondary: var(--swatch--gray-400);
 --_theme---foreground-tertiary: var(--swatch--gray-500);
 --_theme---pictogram-accent: var(--swatch--gray-750);
 --_theme---button-primary--background: var(--swatch--gray-050);
 --_theme---button-primary--text: var(--swatch--gray-950);
 --_theme---button-primary--border: var(--swatch--transparent);
 --_theme---button-primary--icon: var(--_theme---button-primary--text);
 --_theme---button-primary--background-hover: var(--_theme---button-primary--background);
 --_theme---button-primary--text-hover: var(--_theme---button-primary--text);
 --_theme---button-primary--border-hover: var(--_theme---button-primary--border);
 --_theme---button-primary--icon-hover: var(--_theme---background-primary);
 --_theme---button-secondary--background: var(--swatch--gray-750);
 --_theme---button-secondary--text: var(--swatch--gray-050);
 --_theme---button-secondary--border: var(--_theme---border-secondary);
 --_theme---button-secondary--icon: var(--_theme---button-secondary--text);
 --_theme---button-secondary--background-hover: var(--_theme---button-secondary--background);
 --_theme---button-secondary--text-hover: var(--_theme---button-secondary--text);
 --_theme---button-secondary--border-hover: var(--_theme---button-secondary--background);
 --_theme---button-secondary--icon-hover: var(--_theme---foreground-secondary);
 --_theme---button-tertiary--background: var(--_theme---background-primary);
 --_theme---button-tertiary--text: var(--swatch--gray-050);
 --_theme---button-tertiary--border: var(--_theme---border-secondary);
 --_theme---button-tertiary--icon: var(--_theme---button-tertiary--text);
 --_theme---button-tertiary--background-hover: var(--_theme---button-tertiary--background);
 --_theme---button-tertiary--text-hover: var(--_theme---button-tertiary--text);
 --_theme---button-tertiary--border-hover: var(--_theme---button-tertiary--border);
 --_theme---button-tertiary--icon-hover: var(--_theme---foreground-primary);
 --_theme---error-text: #df6666;
 --_theme---heroes-accent: #C46849;
 --_theme---white: var(--_theme---background-primary);
 }
 .u-theme-white,
 [data-wf--section--theme="white"] {
 --_theme---background-primary: var(--swatch--gray-850);
 --_theme---background-secondary: var(--swatch--gray-800);
 --_theme---background-tertiary: var(--swatch--gray-750);
 --_theme---border-primary: var(--swatch--gray-550);
 --_theme---border-secondary: var(--swatch--gray-650);
 --_theme---border-tertiary: var(--swatch--gray-700);
 --_theme---foreground-primary: var(--swatch--gray-050);
 --_theme---foreground-secondary: var(--swatch--gray-350);
 --_theme---foreground-tertiary: var(--swatch--gray-450);
 --_theme---pictogram-accent: var(--swatch--gray-700);
 --_theme---button-primary--background: var(--swatch--gray-050);
 --_theme---button-primary--text: var(--swatch--gray-950);
 --_theme---button-primary--border: var(--swatch--transparent);
 --_theme---button-primary--icon: var(--_theme---button-primary--text);
 --_theme---button-primary--background-hover: var(--_theme---button-primary--background);
 --_theme---button-primary--text-hover: var(--_theme---button-primary--text);
 --_theme---button-primary--border-hover: var(--_theme---button-primary--border);
 --_theme---button-primary--icon-hover: var(--_theme---background-primary);
 --_theme---button-secondary--background: var(--swatch--gray-700);
 --_theme---button-secondary--text: var(--swatch--gray-050);
 --_theme---button-secondary--border: var(--_theme---border-secondary);
 --_theme---button-secondary--icon: var(--_theme---button-secondary--text);
 --_theme---button-secondary--background-hover: var(--_theme---button-secondary--background);
 --_theme---button-secondary--text-hover: var(--_theme---button-secondary--text);
 --_theme---button-secondary--border-hover: var(--_theme---button-secondary--background);
 --_theme---button-secondary--icon-hover: var(--_theme---foreground-secondary);
 --_theme---button-tertiary--background: var(--_theme---background-primary);
 --_theme---button-tertiary--text: var(--swatch--gray-050);
 --_theme---button-tertiary--border: var(--_theme---border-secondary);
 --_theme---button-tertiary--icon: var(--_theme---button-tertiary--text);
 --_theme---button-tertiary--background-hover: var(--_theme---button-tertiary--background);
 --_theme---button-tertiary--text-hover: var(--_theme---button-tertiary--text);
 --_theme---button-tertiary--border-hover: var(--_theme---button-tertiary--border);
 --_theme---button-tertiary--icon-hover: var(--_theme---foreground-primary);
 --_theme---error-text: #df6666;
 --_theme---heroes-accent: #C46849;
 --_theme---white: var(--_theme---background-primary);
 }
 .u-theme-neutral-1,
 [data-wf--section--theme="neutral-1"] {
 --_theme---background-primary: var(--swatch--gray-800);
 --_theme---background-secondary: var(--swatch--gray-750);
 --_theme---background-tertiary: var(--swatch--gray-700);
 --_theme---border-primary: var(--swatch--gray-500);
 --_theme---border-secondary: var(--swatch--gray-600);
 --_theme---border-tertiary: var(--swatch--gray-650);
 --_theme---foreground-primary: var(--swatch--gray-050);
 --_theme---foreground-secondary: var(--swatch--gray-300);
 --_theme---foreground-tertiary: var(--swatch--gray-400);
 --_theme---pictogram-accent: var(--swatch--gray-650);
 --_theme---button-primary--background: var(--swatch--gray-050);
 --_theme---button-primary--text: var(--swatch--gray-950);
 --_theme---button-primary--border: var(--swatch--transparent);
 --_theme---button-primary--icon: var(--_theme---button-primary--text);
 --_theme---button-primary--background-hover: var(--_theme---button-primary--background);
 --_theme---button-primary--text-hover: var(--_theme---button-primary--text);
 --_theme---button-primary--border-hover: var(--_theme---button-primary--border);
 --_theme---button-primary--icon-hover: var(--_theme---background-primary);
 --_theme---button-secondary--background: var(--swatch--gray-650);
 --_theme---button-secondary--text: var(--swatch--gray-050);
 --_theme---button-secondary--border: var(--_theme---border-secondary);
 --_theme---button-secondary--icon: var(--_theme---button-secondary--text);
 --_theme---button-secondary--background-hover: var(--_theme---button-secondary--background);
 --_theme---button-secondary--text-hover: var(--_theme---button-secondary--text);
 --_theme---button-secondary--border-hover: var(--_theme---button-secondary--background);
 --_theme---button-secondary--icon-hover: var(--_theme---foreground-secondary);
 --_theme---button-tertiary--background: var(--_theme---background-primary);
 --_theme---button-tertiary--text: var(--swatch--gray-050);
 --_theme---button-tertiary--border: var(--_theme---border-secondary);
 --_theme---button-tertiary--icon: var(--_theme---button-tertiary--text);
 --_theme---button-tertiary--background-hover: var(--_theme---button-tertiary--background);
 --_theme---button-tertiary--text-hover: var(--_theme---button-tertiary--text);
 --_theme---button-tertiary--border-hover: var(--_theme---button-tertiary--border);
 --_theme---button-tertiary--icon-hover: var(--_theme---foreground-primary);
 --_theme---error-text: #df6666;
 --_theme---heroes-accent: #C46849;
 --_theme---white: var(--_theme---background-primary);
 }

 .logo_light {
 display: none;
 }
 .logo_dark {
 display: block;
 }
 .illustration_light {
 display: none;
 }
 .illustration_dark {
 display: block;
 }

 }

 @media (prefers-color-scheme: light) {
 .logo_light {
 display: block;
 }
 .logo_dark {
 display: none;
 }
 .illustration_light {
 display: block;
 }
 .illustration_dark {
 display: none;
 }
 }

 .u-text-font-mono {
 --_text-style---trim-top: var(--_typography---font--mono-text-trim-top);
 --_text-style---trim-bottom: var(--_typography---font--mono-text-trim-bottom);
 }

 .u-checklist ul {
 list-style: none;
 margin: 0;
 padding: 0;
 }

 .u-checklist ul li {
 position: relative; 
 padding-left: 2rem; 
 }

 .u-checklist ul li::before {
 content: ""; 
 position: absolute;
 left: 0;
 top: 0.1em;
 width: 1.5rem;
 height: 1.5rem;
 background-repeat: no-repeat;
 background-position: center;
 background-size: contain;
 background-image: url("data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%3E%3Cpath%20d%3D%22M18.226%206.13068C18.4439%205.95655%2018.7615%205.95361%2018.9842%206.13888C19.2067%206.32458%2019.2604%206.63728%2019.1283%206.88304L19.0604%206.98382L10.0602%2017.784C9.95233%2017.9133%209.7949%2017.9908%209.62665%2017.9984C9.45844%2018.0059%209.29454%2017.9429%209.17547%2017.8238L4.97541%2013.6237L4.89806%2013.53C4.7446%2013.2971%204.7705%2012.9802%204.97541%2012.7753C5.18032%2012.5704%205.49726%2012.5445%205.73011%2012.698L5.82386%2012.7753L9.55868%2016.5101L18.1393%206.21506L18.226%206.13068Z%22%20fill%3D%22%235E5D59%22/%3E%3C/svg%3E");
 }

 [class^="card_"][class$="_wrap"] .clickable_wrap.u-cover-absolute .clickable_link,
 [class^="card_"][class$="_wrap"] .clickable_wrap.u-cover-absolute .clickable_btn {
 outline-offset: var(--focus--offset-inner);
 }

 textarea[data-autogrow] {
 overflow-y: hidden;
 resize: none;
 height: 1.75rem; 
 min-height: 0; 
 }

 .btn_main_wrap::hover,
 .btn_small_wrap::hover,
 .btn_tiny_wrap::hover,
 .button_toggle_wrap::hover,
 .btn_icon_main_wrap::hover,
 .btn_icon_small_wrap::hover,
 .btn_icon_tiny_wrap::hover{
 transition: /* Transition to click/active */
 box-shadow ease-in-out 100ms, 
 background ease-in-out 100ms,
 color ease-in-out 50ms;
 }

 .btn_main_wrap::active,
 .btn_small_wrap::active,
 .btn_tiny_wrap::active,
 .button_toggle_wrap::active,
 .btn_icon_main_wrap::active,
 .btn_icon_small_wrap::active,
 .btn_icon_tiny_wrap::active{
 transition: /* Transition to click/active */
 box-shadow ease-in-out 50ms, 
 background ease-in-out 50ms,
 color ease-in-out 25ms;
 }

 .card_cs_grid_img img {
 max-width: 60%;
 max-height: 60%;
 }

 @container viewport (width < 30em) {
 [data-wf--grid--column-count="4"]:has(.card_feature_wrap) .c-grid {
 --_column-count---value: 1;
 }
 }
 @container viewport (min-width: 30em) and (max-width: 62em) {
 [data-wf--grid--column-count="4"]:has(.card_feature_wrap) .c-grid {
 --_column-count---value: 2;
 }
 }

 /* Mods for spacing and visibility of embed in accordian content used for schema */
 .accordion_content_text p:has(+ .w-embed.w-script) {
 margin-bottom: 0;
 }

 /* Absolute inner SVG of lottie to prevent page jump */
 .heroes_lottie_component svg {
 position: absolute;
 top: 0;
 left: 0;
 }

 /* Sticky scroll */
 @media screen and (min-width: 992px) {
 .sticky_image_link_wrap:has(.sticky_image_link.w--current) {
 opacity: 1;
 width: calc((100% - var(--_grid---gutter)) * (6 / 12));
 }
 }
 @media screen and (max-width: 767px) {
 .c-grid:last-child .sticky_image_block,
 .sticky_image_block:last-child {
 padding: 0;
 }
 .c-grid:last-child .sticky_image_wrap {
 margin-bottom: 0;
 }
 }

 #send, #threads, #get-help, #collaborate {
 display: block; /* or grid, flex - anything but contents */
 }

 /* Select text below clickable overlay */
 html.wf-design-mode .clickable_wrap {
 pointer-events: none;
 }

 document.addEventListener("DOMContentLoaded", function () {
 // ---------------- Config ----------------
 const EDGE_PADDING = 16; // >= 1rem from edges
 const OFFSET_Y = 10; // gap under trigger
 const DIM_OPACITY = 0.3;
 const DIM_EASE_MS = 350;
 const CLOSE_DELAY = 120;
 const isCoarse = () => matchMedia("(hover: none), (pointer: coarse)").matches;

 // ---------------- Bubble (single instance) ----------------
 function ensureBubble(){
 let el = document.querySelector(".tt-bubble");
 if (el) return el;
 el = document.createElement("div");
 el.className = "tt-bubble u-theme-white";
 el.setAttribute("role","tooltip");
 el.setAttribute("aria-hidden","true");
 el.style.left = "0px";
 el.style.top = "0px";
 el.innerHTML = `
 <div class="tt-inner">
 <div class="tt-h" id="tt-title"></div>
 <p class="tt-b" id="tt-body"></p>
 <button type="button" class="tt-close" aria-label="Close">×</button>
 </div>`;
 document.body.appendChild(el);
 return el;
 }
 const bubble = ensureBubble();
 const elH = bubble.querySelector("#tt-title");
 const elB = bubble.querySelector("#tt-body");
 const elClose = bubble.querySelector(".tt-close");

 // ---------------- Parse [[term|heading|body]] anywhere ----------------
 const TOKEN_RE = /\[\[([^|\]]+)\|([^|\]]+)\|([^\]]+)\]\]/g;
 const BLOCK_SKIP = new Set(["SCRIPT","STYLE","NOSCRIPT","TEXTAREA","INPUT","SELECT","CODE","PRE","TEMPLATE","IFRAME"]);
 function shouldSkipTextNode(n){
 let el = n.parentElement;
 while (el){
 if (BLOCK_SKIP.has(el.tagName) || el.isContentEditable) return true;
 el = el.parentElement;
 }
 return false;
 }
 const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
 const textNodes = [];
 while (walker.nextNode()){
 const n = walker.currentNode;
 if (!n.nodeValue || shouldSkipTextNode(n)) continue;
 if (TOKEN_RE.test(n.nodeValue)) textNodes.push(n);
 TOKEN_RE.lastIndex = 0;
 }
 textNodes.forEach(node => {
 const frag = document.createDocumentFragment();
 const insideLink = !!node.parentElement.closest("a");
 let text = node.nodeValue, last = 0; TOKEN_RE.lastIndex = 0; let m;
 while ((m = TOKEN_RE.exec(text))){
 if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
 const term=m[1].trim(), heading=m[2].trim(), body=m[3].trim();
 const t = insideLink ? document.createElement("span") : document.createElement("button");
 if (insideLink){ t.setAttribute("role","button"); t.setAttribute("tabindex","0"); } else { t.type="button"; }
 t.className="tt-trigger";
 t.textContent=term;
 t.setAttribute("data-tt-h", heading);
 t.setAttribute("data-tt-b", body);
 t.setAttribute("aria-haspopup","dialog");
 t.setAttribute("aria-expanded","false");
 frag.appendChild(t);
 last = TOKEN_RE.lastIndex;
 }
 if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
 node.parentNode.replaceChild(frag, node);
 });

 // ---------------- State ----------------
 let current = null;
 let hoverCount = 0;
 let closeTimer = null;

 // Dimming bookkeeping
 let dimCtx = null; // { container, dimEls:[], wrappedTexts:[], pathEls:[] }

 // ---------------- Find the correct "text element" container ----------------
 function findTextContainer(trigger){
 // Prefer common RTE wrappers
 let el = trigger.closest(".w-richtext, .rich-text, .rte, [data-rte]");
 if (el) return el;

 // Otherwise climb until we find an ancestor that contains multiple block nodes anywhere inside.
 const BLOCK_SEL = "p,h1,h2,h3,h4,h5,h6,ul,ol,li,blockquote,pre,figure,figcaption";
 el = trigger.parentElement;
 while (el && el !== document.body){
 const blockCount = el.querySelectorAll(BLOCK_SEL).length;
 if (blockCount >= 2) return el;
 el = el.parentElement;
 }

 // Fallback: nearest non-inline container
 el = trigger.parentElement || document.body;
 while (el && el !== document.body){
 const d = getComputedStyle(el).display;
 if (d !== "inline" && d !== "contents") return el;
 el = el.parentElement;
 }
 return document.body;
 }

 // Utility: child of `ancestor` that contains `target` (direct child)
 function directChildContaining(ancestor, target){
 for (const ch of ancestor.children){
 if (ch === target || ch.contains(target)) return ch;
 }
 return null;
 }

 function getElementTarget(e) {
 // If target is already an Element, use it
 if (e.target instanceof Element) return e.target;
 // Otherwise, walk the composed/path for the first Element
 const path = (typeof e.composedPath === 'function') ? e.composedPath() : [];
 for (const n of path) if (n instanceof Element) return n;
 return null;
 }

 // ---------------- Dim everything except the trigger branch (sibling branches only) ----------------
 function dimAllOtherBranches(container, trigger){
 undim(); // clear previous

 const dimEls = [];
 const wrappedTexts = [];
 const pathEls = [];

 // Build ELEMENT-only path [container -> ... -> trigger]
 const path = [];
 for (let el = trigger; el && el !== container; el = el.parentElement) path.push(el);
 path.push(container);
 path.reverse();

 // At each ancestor level, find the *direct* child that leads to the trigger
 for (let i = 0; i < path.length; i++){
 const anc = path[i];
 const branchChild = (i < path.length - 1) ? directChildContaining(anc, path[i+1]) : path[i]; // last step is the trigger itself

 // Fade element siblings (whole branches)
 for (const child of anc.children){
 if (child === branchChild) continue; // keep the path branch crisp
 // Never fade any element that is (or contains) the trigger
 if (child === trigger || child.contains(trigger)) continue;
 child.style.transition = `opacity ${DIM_EASE_MS}ms ease`;
 child.style.opacity = String(DIM_OPACITY);
 dimEls.push(child);
 }

 // Fade TEXT NODE siblings directly under this ancestor (outside branchChild)
 anc.childNodes.forEach(node => {
 if (node.nodeType !== 3) return; // text only
 if (!node.nodeValue || !node.nodeValue.trim()) return;
 // If this text node sits inside branchChild, skip
 if (branchChild && branchChild.contains && branchChild.contains(node)) return;
 const span = document.createElement("span");
 span.style.transition = `opacity ${DIM_EASE_MS}ms ease`;
 span.style.opacity = String(DIM_OPACITY);
 span.textContent = node.nodeValue;
 node.parentNode.replaceChild(span, node);
 wrappedTexts.push(span);
 });

 // Keep a reference to the path elements (so we can explicitly restore opacity if needed)
 if (anc && anc.nodeType === 1) pathEls.push(anc);
 }

 // Hard-guard: explicitly set opacity:1 on the entire path to neutralize any inherited fade
 pathEls.forEach(el => {
 el.style.opacity = "1";
 });

 dimCtx = { container, dimEls, wrappedTexts, pathEls };
 }

 function undim(){
 if (!dimCtx) return;
 const { dimEls, wrappedTexts, pathEls } = dimCtx;

 // Animate back
 dimEls.forEach(el => {
 el.style.transition = `opacity ${DIM_EASE_MS}ms ease`;
 el.style.opacity = "1";
 // remove inline style after the animation so we don't override site CSS
 setTimeout(() => { if (el) el.style.opacity = ""; }, DIM_EASE_MS + 50);
 });

 wrappedTexts.forEach(span => {
 span.style.transition = `opacity ${DIM_EASE_MS}ms ease`;
 span.style.opacity = "1";
 span.addEventListener("transitionend", () => {
 if (!span.parentNode) return;
 span.parentNode.replaceChild(document.createTextNode(span.textContent || ""), span);
 }, { once:true });
 });

 // Clear hard-guard on path
 pathEls.forEach(el => { if (el) el.style.opacity = ""; });

 dimCtx = null;
 }

 // ---------------- Positioning (centered, edge-aware, flip) ----------------
 function clamp(v,min,max){ return Math.max(min,Math.min(max,v)); }
 function measureBubbleForPlacement(){
 const wasOpen = bubble.classList.contains("is-open");
 if (!wasOpen){ bubble.style.visibility="hidden"; bubble.classList.add("is-open"); }
 const rect = bubble.getBoundingClientRect();
 if (!wasOpen){ bubble.classList.remove("is-open"); bubble.style.visibility=""; }
 return { w: rect.width, h: rect.height };
 }
 function placeAnchored(trigger){
 const vw=innerWidth, vh=innerHeight;
 const r = trigger.getBoundingClientRect();
 const { w, h } = measureBubbleForPlacement();

 let left = r.left + (r.width/2) - (w/2);
 left = clamp(left, EDGE_PADDING, Math.max(EDGE_PADDING, vw - EDGE_PADDING - w));

 const topBelow = r.bottom + OFFSET_Y;
 const spaceBelow = vh - topBelow - EDGE_PADDING;
 const placeBelow = spaceBelow >= h;
 let top = placeBelow ? topBelow : (r.top - h - OFFSET_Y);
 top = clamp(top, EDGE_PADDING, Math.max(EDGE_PADDING, vh - EDGE_PADDING - h));

 bubble.style.left = left + "px";
 bubble.style.top = top + "px";

 const br = bubble.getBoundingClientRect();
 if (br.bottom > vh - EDGE_PADDING){
 bubble.style.maxHeight = (vh - 2*EDGE_PADDING) + "px";
 bubble.style.overflowY = "auto";
 } else {
 bubble.style.maxHeight = "none";
 bubble.style.overflowY = "visible";
 }
 }

 // ---------------- Open / Close (place → fade/scale) ----------------
 function animateIn(){
 bubble.style.transition = "none";
 bubble.style.opacity = "0";
 bubble.style.transform = "scale(0.95)";
 void bubble.offsetWidth;
 bubble.style.transition = "opacity .18s ease, transform .18s ease";
 bubble.style.opacity = "1";
 bubble.style.transform = "scale(1)";
 }
 function animateOut(done){
 bubble.style.transition = "opacity .16s ease, transform .16s ease";
 bubble.style.opacity = "0";
 bubble.style.transform = "scale(0.95)";
 const end = () => { bubble.removeEventListener("transitionend", end); done && done(); };
 bubble.addEventListener("transitionend", end);
 setTimeout(end, 260);
 }

 function openFromTrigger(trigger){
 if (current && current !== trigger) forceClose();
 current = trigger;
 trigger.setAttribute("aria-expanded","true");

 elH.textContent = trigger.getAttribute("data-tt-h") || "";
 elB.textContent = trigger.getAttribute("data-tt-b") || "";

 bubble.classList.add("is-open");
 bubble.setAttribute("aria-hidden","false");

 placeAnchored(trigger);
 animateIn();

 const container = findTextContainer(trigger);
 dimAllOtherBranches(container, trigger);

 hoverCount = 0;
 cancelCloseTimer();
 }

 function forceClose(){
 if (!current) return;
 bubble.classList.remove("is-open");
 bubble.setAttribute("aria-hidden","true");
 current.setAttribute("aria-expanded","false");
 current = null;
 undim();
 hoverCount = 0;
 cancelCloseTimer();
 }

 function closeWithAnim(){
 if (!current) return;
 const t = current;
 animateOut(() => {
 bubble.classList.remove("is-open");
 bubble.setAttribute("aria-hidden","true");
 t.setAttribute("aria-expanded","false");
 current = null;
 undim();
 });
 }

 function scheduleClose(){
 cancelCloseTimer();
 closeTimer = setTimeout(() => {
 if (hoverCount <= 0 && !isCoarse()) closeWithAnim();
 }, CLOSE_DELAY);
 }
 function cancelCloseTimer(){ if (closeTimer){ clearTimeout(closeTimer); closeTimer = null; } }

 // ---------------- Hover-intent (desktop) ----------------
 function onZoneEnter(){ if (isCoarse()) return; hoverCount++; cancelCloseTimer(); }
 function onZoneLeave(){ if (isCoarse()) return; hoverCount = Math.max(0, hoverCount - 1); if (hoverCount === 0) scheduleClose(); }

 bubble.addEventListener("pointerenter", onZoneEnter, true);
 bubble.addEventListener("mouseenter", onZoneEnter, true);
 bubble.addEventListener("pointerleave", onZoneLeave, true);
 bubble.addEventListener("mouseleave", onZoneLeave, true);

 const handleEnter = (e) => {
 if (isCoarse()) return;
 const target = getElementTarget(e);
 if (!target) return;
 const t = target.closest(".tt-trigger");
 if (!t) return;
 onZoneEnter();
 if (!current || current !== t) openFromTrigger(t);
 };
 const handleLeave = (e) => {
 if (isCoarse()) return;
 const target = getElementTarget(e);
 if (!target) return;
 const t = target.closest(".tt-trigger");
 if (!t) return;
 onZoneLeave();
 };
 document.addEventListener("pointerenter", handleEnter, true);
 document.addEventListener("mouseenter", handleEnter, true);
 document.addEventListener("pointerleave", handleLeave, true);
 document.addEventListener("mouseleave", handleLeave, true);

 // ---------------- Keyboard ----------------
 document.addEventListener("focusin", (e) => {
 if (!e.target) return;
 const t = e.target.closest(".tt-trigger");
 if (t) openFromTrigger(t);
 });
 document.addEventListener("focusout", (e) => {
 if (!e.target) return;
 const t = e.target.closest(".tt-trigger");
 if (t && current === t) closeWithAnim();
 });

 // ---------------- Mobile / coarse ----------------
 document.addEventListener("pointerdown", (e) => {
 if (!isCoarse()) return;

 const t = e.target.closest(".tt-trigger");
 if (!t) return;
 e.preventDefault();
 e.stopPropagation();
 if (current === t && bubble.classList.contains("is-open")) { closeWithAnim(); return; }
 openFromTrigger(t);
 }, true);

 document.addEventListener("click", (e) => {
 if (!isCoarse()) return;
 if (!bubble.classList.contains("is-open")) return;
 const inBubble = !!e.target.closest(".tt-bubble");
 const onTrigger = !!e.target.closest(".tt-trigger");
 if (!inBubble && !onTrigger) closeWithAnim();
 }, true);

 // Close button + ESC
 elClose.addEventListener("click", closeWithAnim);
 document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeWithAnim(); });

 // Reposition on resize/scroll while open
 const reposition = () => { if (!current) return; placeAnchored(current); };
 addEventListener("resize", reposition, { passive: true });
 addEventListener("scroll", reposition, { passive: true });
 });
 
/* Tooltip Styles */

 /* Trigger */
 .tt-trigger {
 cursor: help;
 text-decoration: underline dotted;
 text-underline-offset: .2em;
 color: inherit;
 }
 .tt-trigger:focus-visible{ outline:2px solid currentColor; outline-offset:2px; }

 /* Bubble */
 .tt-bubble{
 position: fixed;
 z-index: 10;
 max-width: 17rem;
 background: var(--_theme---background-primary);
 box-shadow: 0 4px 24px rgba(0,0,0,.05);
 border-radius: var(--radius--large);
 border-style: solid;
 border-color: var(--_theme---border-tertiary);
 padding: var(--_spacing---space--1-5rem);
 pointer-events: none;
 opacity: 0;
 transform: translate3d(0,0,0) scale(.98);
 transition: opacity .3s ease, transform .3s ease;
 will-change: transform, opacity;
 }
 .tt-bubble.is-open{ opacity:1; transform:translate3d(0,0,0) scale(1); pointer-events:auto; }

 .tt-h{ 
 margin-bottom: var(--_spacing---space--0-5rem); 
 font-size: var(--_typography---font-size--body-3); 
 font-family: var(--_typography---font--secondary-family);
 line-height: var(--_typography---line-height--1-6); 
 color: var(--_theme---foreground-primary);
 }
 .tt-b{ 
 margin:0; 
 font-size: var(--_typography---font-size--caption);
 line-height: var(--_typography---line-height--1-6);
 color: var(--_theme---foreground-tertiary);
 }

 /* Mobile close button */
 .tt-close {
 display: none;
 }
 @media (hover: none), (pointer: coarse) {
 .tt-close {
 display: inline-flex;
 position: absolute;
 top: 0.5rem;
 right: 0.5rem;
 width: 32px;
 height: 32px;
 align-items: center;
 justify-content: center;
 border: 0;
 border-radius: 999px;
 background: transparent;
 font-size: 22px; 
 line-height: 1;
 color: inherit;
 cursor: pointer;
 touch-action: manipulation;
 }
 .tt-close:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
 .tt-close:hover { opacity: 1; }
 }

 html[lang="de-DE"] h1, html[lang="de-DE"] h2, html[lang="de-DE"] h3, 
 html[lang="de-DE"] h4, html[lang="de-DE"] h5, html[lang="de-DE"] h6,
 html[lang="de-DE"] p, html[lang="de-DE"] li,
 html[lang="fr-FR"] h1, html[lang="fr-FR"] h2, html[lang="fr-FR"] h3,
 html[lang="fr-FR"] h4, html[lang="fr-FR"] h5, html[lang="fr-FR"] h6,
 html[lang="fr-FR"] p, html[lang="fr-FR"] li {
 overflow-wrap: break-word;
 hyphens: auto;
 }

 :root {
 --nav--icon-thickness: var(--border-width--main);
 --nav--hamburger-thickness: var(--nav--icon-thickness);
 --nav--hamburger-gap: var(--_spacing---space--0-25rem);
 --nav--hamburger-rotate: 45;
 --nav--dropdown-duration: 300ms;
 --nav--dropdown-open-duration: 600ms;
 --nav--dropdown-delay: 0ms;
 --ease-expo-out: cubic-bezier(0.16, 1, 0.3, 1);
 }

 /* ========== GENERAL RESPONSIVE RULES ========== */

 /* Lock body when nav is open (script toggles .is-nav-open) */
 @media (width < 56em) {
 body.is-nav-open { overflow: hidden; }
 }

 @container (min-width: 56em) {
 .nav_wrap.is-desktop { display: block; }
 .nav_wrap.is-mobile { display: none; }
 }
 @container (width < 28em) {
 .nav_mobile_layout .nav_actions_mobile { display: none; }
 }

 /* ========== DROPDOWN STYLING ========== */

 html:not(.wf-design-mode) .nav_dropdown_component > .w-dropdown-list {
 display: grid !important;
 grid-template-columns: minmax(0, 1fr);
 grid-template-rows: 0fr;
 transition:
 grid-template-rows var(--nav--dropdown-duration) var(--ease-expo-out),
 visibility 0s var(--nav--dropdown-duration),
 opacity var(--nav--dropdown-duration) var(--ease-expo-out);
 visibility: hidden;
 opacity: 0;
 }
 html:not(.wf-design-mode) .nav_dropdown_component > .w-dropdown-list.w--open {
 visibility: visible;
 opacity: 1;
 transition:
 grid-template-rows var(--nav--dropdown-duration) var(--ease-expo-out),
 visibility 0s 0s,
 opacity var(--nav--dropdown-duration) var(--ease-expo-out);
 }
 .nav_dropdown_component > .w-dropdown-list > * { overflow: hidden; }
 .nav_dropdown_component:has(> .w-dropdown-toggle[aria-expanded="true"]) > .w-dropdown-list {
 --nav--dropdown-duration: var(--nav--dropdown-open-duration);
 grid-template-rows: 1fr;
 }
 /*.nav_wrap.is-desktop:has(.nav_dropdown_component > .w-dropdown-toggle.w--open[aria-expanded="false"])
 .nav_dropdown_component:has(> .w--open[aria-expanded="true"]) > .w-dropdown-list {
 transition-delay: var(--nav--dropdown-duration);
 }*/

 /* Dropdown caret rotation */
 .nav_links_svg.is-desktop { transition: transform 750ms var(--ease-expo-out); }
 .w-dropdown-toggle[aria-expanded="true"] .nav_links_svg.is-desktop { transform: rotate(-180deg); }

 .nav_links_svg_line.is-2 { transition: transform 500ms var(--ease-expo-out); }
 .w-dropdown-toggle[aria-expanded="true"] .nav_links_svg_line.is-2 { transform: rotate(0deg); }

 /* open (replicates your original transforms) */
 .nav_btn_wrap[aria-expanded="true"] .nav_btn_line:nth-child(1),
 .nav_btn_wrap[aria-expanded="true"] > * > :first-child {
 transform:
 translateY(calc(var(--nav--hamburger-thickness) * 1 + var(--nav--hamburger-gap) * 1))
 rotate(calc(var(--nav--hamburger-rotate) * -1deg));
 }
 .nav_btn_wrap[aria-expanded="true"] .nav_btn_line:nth-child(2),
 .nav_btn_wrap[aria-expanded="true"] > * > :nth-child(2) {
 opacity: 0;
 }
 .nav_btn_wrap[aria-expanded="true"] .nav_btn_line:nth-child(3),
 .nav_btn_wrap[aria-expanded="true"] > * > :last-child {
 transform:
 translateY(calc(var(--nav--hamburger-thickness) * -1 + var(--nav--hamburger-gap) * -1))
 rotate(calc(var(--nav--hamburger-rotate) * 1deg));
 width: 1rem;
 }

 /* ========== HOVER & THEME EFFECTS ========== */
 @media (hover: hover) and (pointer: fine) {
 body:has(.nav_dropdown_item:hover) .nav_dropdown_item:not(:hover) > * > * {
 color: var(--_theme---foreground-tertiary);
 }
 .nav_dropdown_link {
 transition:
 background-color 300ms ease,
 color 300ms ease;
 }
 .nav_dropdown_item:hover .nav_dropdown_link {
 background: var(--_theme---background-tertiary);
 color: var(--_theme---foreground-primary);
 }
 .nav_secondary_wrap .nav_dropdown_item:hover .nav_dropdown_link {
 background: var(--_theme---background-tertiary);
 color: var(--_theme---foreground-primary);
 }
 .nav_wrap.is-mobile .nav_dropdown_item:hover .nav_dropdown_link {
 color: var(--_theme---foreground-primary);
 }
 .nav_links_text { transition: color 500ms var(--ease-expo-out); }
 .nav_links_svg {
 transition:
 transform 500ms var(--ease-expo-out),
 color 500ms var(--ease-expo-out);
 }
 .nav_links_item:hover .nav_links_text,
 .nav_links_item:hover .nav_links_svg { color: var(--_theme---foreground-primary); }
 }

 /* ========== LAYOUT / UTILITY (kept, de-Webflow’d) ========== */
 .nav_wrap.is-mobile [data-open-on-mobile] > .w-dropdown-toggle { display: none; }
 .nav_wrap.is-mobile [data-open-on-mobile] > .w-dropdown-list {
 visibility: visible;
 opacity: 1;
 display: block;
 grid-template-rows: 1fr;
 }
 .nav_buttons_item .button_main_wrap { width: 100%; min-width: max-content; }

 /* Optional: fade out mobile actions while open */
 .nav_actions_wrap { transition: opacity 500ms var(--ease-expo-out); }
 body.is-nav-open .nav_actions_mobile .nav_actions_wrap {
 opacity: 0;
 pointer-events: none;
 }

 .nav_links_item:first-child {
 border-top: none;
 }

 /* ========== Breadcrumbs ========== */
 .breadcrumb_text.is_linked[href="#"],
 .breadcrumb_text:has(+.breadcrumb_text.is_linked:not([href="#"])) {
 display: none;
 }
 .breadcrumb_text.is_linked:not([href="#"]) {
 display: block;
 }

document.addEventListener("DOMContentLoaded", function () {
 document.querySelectorAll(".nav_component").forEach((root) => {
 if (root.dataset.scriptInitialized) return;
 root.dataset.scriptInitialized = "true";

 if (!window.gsap) { console.error("GSAP not found"); return; }

 const btn = root.querySelector('.nav_btn_wrap');
 const menu = root.querySelector('.nav_menu_wrap');
 if (!btn || !menu) { console.warn('Missing .nav_btn_wrap or .nav_menu_wrap in', root); return; }

 // a11y setup (scoped)
 if (!btn.hasAttribute('type')) btn.setAttribute('type', 'button');
 if (!btn.hasAttribute('aria-expanded')) btn.setAttribute('aria-expanded', 'false');
 if (!menu.id) menu.id = 'primary-nav-' + Math.random().toString(36).slice(2);
 if (!btn.hasAttribute('aria-controls')) btn.setAttribute('aria-controls', menu.id);
 menu.setAttribute('aria-hidden', 'true');

 // targets (scoped)
 const items = Array.from(menu.querySelectorAll('.nav_links_item'));
 const actions = menu.querySelector('.nav_menu_actions_wrap');

 // feature detection
 const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 const canClipInset = !!(window.CSS && CSS.supports && (
 CSS.supports('clip-path','inset(0 0 100% 0)') || CSS.supports('-webkit-clip-path','inset(0 0 100% 0)')
 ));
 const useClip = canClipInset && !prefersReduced;

 // durations from CSS vars
 function readDur(varName, fallbackSec) {
 const v = getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
 if (!v) return fallbackSec;
 if (v.endsWith('ms')) return parseFloat(v)/1000;
 if (v.endsWith('s')) return parseFloat(v);
 const n = parseFloat(v);
 return isNaN(n) ? fallbackSec : n;
 }
 const OPEN_DUR = readDur('--nav--menu-open-duration', 0.8);
 const CLOSE_DUR = readDur('--nav--menu-close-duration', 0.4);

 // state per component
 let isOpen = false;
 let current = null;

 function setMenuVisibleForAnim() {
 menu.style.display = 'flex'; // ensure it's shown before anim
 menu.removeAttribute('hidden');
 menu.setAttribute('aria-hidden', 'false');
 menu.style.willChange = useClip ? 'clip-path' : 'transform, opacity';
 }
 function clearMenuInline() {
 gsap.set(menu, { clearProps: 'clipPath,webkitClipPath,opacity,transform,willChange,pointerEvents' });
 }

 // OPEN
 function playOpen() {
 setMenuVisibleForAnim();
 menu.style.pointerEvents = 'none';
 document.body.classList.add('is-nav-open');
 btn.setAttribute('aria-expanded', 'true');

 if (useClip) {
 gsap.set(menu, { clipPath: 'inset(0 0 100% 0)', webkitClipPath: 'inset(0 0 100% 0)' });
 } else {
 gsap.set(menu, { yPercent: -2, opacity: 0 });
 }
 if (items.length) gsap.set(items, { y: 20, autoAlpha: 0 });
 if (actions) gsap.set(actions, { y: 20, autoAlpha: 0 });

 const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

 if (useClip) {
 tl.to(menu, {
 clipPath: 'inset(0 0 0% 0)',
 webkitClipPath: 'inset(0 0 0% 0)',
 duration: prefersReduced ? 0.01 : OPEN_DUR,
 ease: 'expo.out'
 }, 0);
 } else {
 tl.to(menu, { yPercent: 0, opacity: 1, duration: prefersReduced ? 0.01 : Math.min(OPEN_DUR, 0.36) }, 0.02);
 }

 if (items.length) {
 tl.to(items, { y: 0, autoAlpha: 1, stagger: prefersReduced ? 0 : 0.08, duration: prefersReduced ? 0.01 : 0.4 }, 0.10);
 }
 if (actions) {
 const base = 0.10 + (items.length ? items.length * (prefersReduced ? 0 : 0.08) : 0);
 tl.to(actions, { y: 0, autoAlpha: 1, duration: prefersReduced ? 0.01 : 0.4 }, base);
 }

 tl.add(() => { menu.style.pointerEvents = 'auto'; }, '>-0.1');

 // listeners (per open)
 document.addEventListener('keydown', onKeydown);
 menu.addEventListener('click', onMenuLinkClick);

 return tl;
 }

 // CLOSE (fade all together, then clip inset close)
 function playClose() {
 menu.style.pointerEvents = 'none';
 btn.setAttribute('aria-expanded', 'false');
 document.body.classList.remove('is-nav-open');

 const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

 const fadeTargets = items.concat(actions ? [actions] : []);
 if (fadeTargets.length) tl.to(fadeTargets, { autoAlpha: 0, y: 0, duration: prefersReduced ? 0.01 : 0.2 }, 0);

 if (useClip) {
 gsap.set(menu, { clipPath: 'inset(0 0 0% 0)', webkitClipPath: 'inset(0 0 0% 0)' });
 tl.to(menu, {
 clipPath: 'inset(0 0 100% 0)',
 webkitClipPath: 'inset(0 0 100% 0)',
 duration: prefersReduced ? 0.01 : CLOSE_DUR
 }, '>-0.02');
 } else {
 tl.to(menu, { yPercent: -2, opacity: 0, duration: prefersReduced ? 0.01 : Math.min(CLOSE_DUR, 0.28) }, '>-0.02');
 }

 tl.add(() => {
 menu.style.display = 'none';
 menu.setAttribute('aria-hidden', 'true');
 clearMenuInline();
 if (items.length) gsap.set(items, { clearProps: 'all' });
 if (actions) gsap.set(actions, { clearProps: 'all' });

 // remove listeners added on open
 document.removeEventListener('keydown', onKeydown);
 menu.removeEventListener('click', onMenuLinkClick);
 });

 return tl;
 }

 function openMenu() {
 if (isOpen) return;
 isOpen = true;
 if (current && current.isActive()) current.kill();
 current = playOpen();
 }
 function closeMenu() {
 if (!isOpen) return;
 isOpen = false;
 if (current && current.isActive()) current.kill();
 current = playClose();
 }

 function onKeydown(e){ if (e.key === 'Escape' && isOpen) { e.preventDefault(); closeMenu(); } }

 function onMenuLinkClick(e){
 const a = e.target.closest('a[href]');
 if (!a) return;
 const url = new URL(a.href, location.href);
 if (url.origin === location.origin) {
 e.preventDefault();
 const tl = playClose();
 tl.eventCallback('onComplete', () => { window.location.href = a.href; });
 isOpen = false;
 }
 }

 // Toggle (scoped)
 btn.addEventListener('click', () => (isOpen ? closeMenu() : openMenu()));

 // Normalize if visible on load (scoped)
 if (getComputedStyle(menu).display !== 'none') {
 btn.setAttribute('aria-expanded', 'true');
 menu.setAttribute('aria-hidden', 'false');
 document.body.classList.add('is-nav-open');
 isOpen = true;
 }
 });
});

 (function () {
 'use strict';

 // ---------- tiny utils ----------
 var NS = 'navBundleInit';
 function onceFlag(el, k){ k=k||'scriptInitialized'; if (el.dataset[k]) return true; el.dataset[k]='true'; return false; }
 function ready(fn){ if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',fn,{once:true});} else { fn(); } }

 // ---------- 1) Ask Claude about this page ----------
 function initAskPage(){
 var buttons = document.querySelectorAll('[data-ask-page]');
 if (!buttons.length) return; // Early exit if no buttons

 buttons.forEach(function(btn){
 if (onceFlag(btn, NS)) return;
 btn.addEventListener('click', function (e) {
 e.preventDefault();
 var pageUrl = window.location.href;
 var prompt = "Read this page " + pageUrl + " so that I can ask you questions about it";
 var claudeUrl = new URL('https://claude.ai/new');
 claudeUrl.searchParams.set('q', prompt);
 window.open(claudeUrl.toString(), '_blank', 'noopener');
 });
 });
 }

 // ---------- 2) Copy page content as Markdown (Turndown) ----------
 var _turndownReady;
 function ensureTurndown(){
 if (window.TurndownService) return Promise.resolve();
 if (_turndownReady) return _turndownReady;
 _turndownReady = new Promise(function(resolve, reject){
 var s = document.createElement('script');
 s.src = 'https://unpkg.com/turndown/dist/turndown.js';
 s.async = true;
 s.onload = function(){ resolve(); };
 s.onerror = function(){ reject(new Error('Failed to load Turndown')); };
 document.head.appendChild(s);
 });
 return _turndownReady;
 }

 function initCopyAsMarkdown(){
 var copyButton = document.getElementById('copy-as-markdown');
 if (!copyButton) return; // Early exit

 if (onceFlag(copyButton, NS)) return;

 var buttonTextEl = copyButton.querySelector('.nav_dropdown_text') || copyButton;
 var originalText = buttonTextEl.textContent;

 copyButton.addEventListener('click', function(){
 ensureTurndown().then(function(){
 try {
 var TurndownService = window.TurndownService;
 var turndownService = new TurndownService({
 headingStyle: 'atx',
 codeBlockStyle: 'fenced',
 fence: '```',
 emDelimiter: '*',
 strongDelimiter: '**',
 linkStyle: 'inlined'
 });

 // Skip junk
 turndownService.addRule('skipWebflowElements', {
 filter: function(node){
 return node.nodeName === 'SCRIPT' ||
 node.nodeName === 'STYLE' ||
 (node.className && (String(node.className).includes('w-editor') || String(node.className).includes('w-embed')));
 },
 replacement: function(){ return ''; }
 });

 buttonTextEl.textContent = 'Copying...';
 copyButton.disabled = true;

 var contentElement = document.querySelector('main') ||
 document.querySelector('.main-content') ||
 document.querySelector('body');
 if (!contentElement) throw new Error('No content found to copy');

 var cloned = contentElement.cloneNode(true);
 cloned.querySelectorAll('script, style, nav, footer, .w-nav, .footer').forEach(function(el){ el.remove(); });

 var markdown = turndownService.turndown(cloned);

 var done = function(){
 buttonTextEl.textContent = 'Copied!';
 setTimeout(function(){
 buttonTextEl.textContent = originalText;
 copyButton.disabled = false;
 }, 2000);
 };

 if (navigator.clipboard && window.isSecureContext) {
 navigator.clipboard.writeText(markdown).then(done, function(err){ throw err; });
 } else {
 var ta = document.createElement('textarea');
 ta.value = markdown; ta.style.position='fixed'; ta.style.opacity='0';
 document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta);
 done();
 }
 } catch (err){
 console.error('Copy failed:', err);
 buttonTextEl.textContent = 'Copy failed';
 setTimeout(function(){
 buttonTextEl.textContent = originalText;
 copyButton.disabled = false;
 }, 2000);
 }
 }).catch(function(err){
 console.error('Turndown load failed:', err);
 buttonTextEl.textContent = 'Copy failed';
 setTimeout(function(){
 buttonTextEl.textContent = originalText;
 copyButton.disabled = false;
 }, 2000);
 });
 });
 }

 // ---------- init all ----------
 ready(function(){
 initAskPage();
 initCopyAsMarkdown();
 });

 // Optional: expose minimal API for debugging (comment out in production if not needed)
 // window.NavBundle = {
 // initCopyAsMarkdown: initCopyAsMarkdown,
 // initAskPage: initAskPage
 // };
 })();
Explore here
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - 
THUMBNAIL BG COLORS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - */
[data-thumbnail-bg="Clay"] { background-color: var(--swatch--clay); }
[data-thumbnail-bg="Cactus"] { background-color: var(--swatch--cactus); }
[data-thumbnail-bg="Coral"] { background-color: var(--swatch--coral); }
[data-thumbnail-bg="Fig"] { background-color: var(--swatch--fig); }
[data-thumbnail-bg="Heather"] { background-color: var(--swatch--heather); }
[data-thumbnail-bg="Oat"] { background-color: var(--swatch--oat); }
[data-thumbnail-bg="Olive"] { background-color: var(--swatch--olive); }
[data-thumbnail-bg="Sky"] { background-color: var(--swatch--sky); }

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - 
CONDITIONAL STYLES BASED ON IF IMAGE OR VIDEO ARE VISIBLE
- - - - - - - - - - - - - - - - - - - - - - - - - - - - */
.hero_tutorial_post_wrap:has(+ .tutorial_post_media_wrap :is(.tutorial_post_image_wrap, .tutorial_post_video_wrap):not(.w-condition-invisible)) {
 border-bottom: none !important;
}

.tutorial_post_media_wrap:has(+ .tutorial_post_wrap:not(.w-condition-invisible)) .u-section-spacer {
 display: none !important;
}

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - 
TABLE OF CONTENTS
Adding here so classes don't get accidentally cleared
- - - - - - - - - - - - - - - - - - - - - - - - - - - - */
.tutorial_post_toc_list {
 color: var(--_theme---foreground-tertiary); 
 font-size: var(--_typography---font-size--body-3);
}

.tutorial_post_toc_item {
 margin-left: -0.0625rem; 
 padding-top: var(--_spacing---space--0-25rem);
 padding-bottom: var(--_spacing---space--0-25rem); 
 padding-left: var(--_spacing---space--1rem); 
 border-left-style: solid; 
 border-left-width: var(--border-width--main); 
 border-left-color: var(--_theme---border-secondary);
}

.tutorial_post_toc_item.active {
 border-left-color: var(--_theme---heroes-accent);
}

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - 
ANCHOR LINK
- - - - - - - - - - - - - - - - - - - - - - - - - - - - */
/* offset for <span class="anchor"> that takes fixed header height into account */
.anchor { 
 position: relative;
 top: calc(-1 * var(--_spacing---space--4rem) - 120px); 
}
/* Copy anchor link to clipboard button */
.anchor-link-box {
 /* quick btn reset */
 background: none;
 border: none;
 padding: 0;
 cursor: pointer;
 /* other styles */
 position: absolute !important;
 left: -3rem;
 top: 50%;
 transform: translateY(-50%);
 opacity: 0;
 transition: opacity 0.2s ease;
 width: 2.5rem;
 height: 2.5rem;
 background: var(--_theme---background-tertiary);
 border: var(--border-width--main) solid var(--_theme---border-tertiary);
 border-radius: var(--radius--main);
 display: flex;
 align-items: center;
 justify-content: center;
 padding: var(--_spacing---space--0-5rem);
}

.anchor-link-box:hover {
 opacity: 1;
}

.tooltip {
 opacity: 0;
 transition: opacity 0.2s ease;
 position: absolute;
 left: 50%;
 bottom: calc(100% + 0.5rem);
 transform: translateX(-50%);
 background: var(--_theme---button-primary--background);
 color: var(--_theme---button-primary--text);
 white-space: nowrap;
 padding: 0.125rem 0.5rem;
 border-radius: var(--radius--x-small);
 font-family: var(--_typography---font--primary-family);
 font-size: var(--_typography---font-size--caption);
 line-height: var(--_typography---line-height--1-6);
}

.tooltip.active {
 opacity: 1;
}

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - 
HIDE EMPTY <p> TAGS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - */
p:empty,
p:has(> br:only-child) {
 display: none;
}

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - 
BORDER RADIUS ON RICH TEXT VIDEOS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - */
.w-richtext-figure-type-video {
 border-radius: var(--radius--main);
 overflow: hidden;
}
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - 
FIX GRID SPACING IF TUTORIAL HAS NO VIDEO
- - - - - - - - - - - - - - - - - - - - - - - - - - - - */
.tutorial_post_video_layout:has(.w-dyn-bind-empty) {
 display: none;
}

document.addEventListener('DOMContentLoaded', function() {
 // Helper function to convert text to slug
 function textToSlug(text) {
 return text
 .toLowerCase()
 .trim()
 .replace(/[''"&]/g, '')
 .replace(/"([^"]+)"/, '$1')
 .replace(/\s*[:.,?—–\\/-]\s*/g, '-')
 .replace(/\s+/g, '-')
 .replace(/-+/g, '-')
 .replace(/^-+|-+$/g, '');
 }
 
 // Track used slugs to prevent duplicate IDs
 const usedSlugs = new Set();
 
 function getUniqueSlug(baseSlug) {
 let slug = baseSlug;
 let counter = 1;
 while (usedSlugs.has(slug)) {
 slug = `${baseSlug}-${counter}`;
 counter++;
 }
 usedSlugs.add(slug);
 return slug;
 }
 
 // Add/Remove class helper functions
 const addClass = (element, className) => {
 if (element && className) {
 element.classList.add(className);
 }
 };
 
 const removeClass = (element, className) => {
 if (element && className) {
 element.classList.remove(className);
 }
 };
 
 // Debounce helper for resize events
 function debounce(func, wait) {
 let timeout;
 return function executedFunction(...args) {
 const later = () => {
 clearTimeout(timeout);
 func(...args);
 };
 clearTimeout(timeout);
 timeout = setTimeout(later, wait);
 };
 }
 
 // Get elements
 const tutorialContent = document.getElementById('tutorial_content');
 const tocContainer = document.getElementById('tutorial_toc');
 
 if (!tutorialContent || !tocContainer) {
 return;
 }
 
 const h2Elements = tutorialContent.querySelectorAll('h2');
 
 if (h2Elements.length === 0) {
 tocContainer.style.display = 'none';
 return;
 }
 
 // Create ToC list
 const tocList = document.createElement('ul');
 addClass(tocList, 'tutorial_post_toc_list');
 
 const tocItems = [];
 
 // Copy anchor link to clipboard with tooltip
 const copyAnchorToClipboard = (element, spanElement, mouseEnterTime = 750) => {
 let hoverTimeout;
 let tooltip;
 
 element.addEventListener("mouseenter", function () {
 clearTimeout(hoverTimeout);
 tooltip = document.createElement("span");
 addClass(tooltip, 'tooltip');
 tooltip.innerText = "Copy anchor link";
 this.appendChild(tooltip);
 hoverTimeout = setTimeout(() => {
 addClass(tooltip, "active");
 }, mouseEnterTime);
 });

 element.addEventListener("mouseleave", function () {
 clearTimeout(hoverTimeout);
 if (tooltip) {
 removeClass(tooltip, "active");
 this.removeChild(tooltip);
 tooltip = null;
 }
 });

 element.addEventListener("click", function (event) {
 event.preventDefault();
 clearTimeout(hoverTimeout);

 if (spanElement && spanElement.classList.contains("anchor")) {
 const id = spanElement.id;

 if (tooltip) {
 tooltip.innerText = "Copied!";
 addClass(tooltip, "active");

 const url = new URL(window.location.href);
 url.searchParams.delete("topic");
 const anchorLink = `${url.origin}${url.pathname}#${id}`;

 if (navigator && navigator.clipboard) {
 navigator.clipboard.writeText(anchorLink).catch((err) => {
 console.error("Could not copy text: ", err);
 });
 }
 hoverTimeout = setTimeout(() => {
 removeClass(tooltip, "active");
 }, 1500);
 }
 } else {
 console.error("Couldn't find Span with the ID");
 }
 });
 };
 
 // Anchor link SVG icon
 const anchorLinkSVG = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M7.59608 7.99088C9.01909 7.43035 10.5884 7.86617 11.5326 8.96256L11.7123 9.19108C11.7695 9.27004 11.8243 9.35165 11.8754 9.4362L12.018 9.69792L12.0531 9.79362C12.1116 10.0184 12.0068 10.2611 11.7904 10.3678C11.5738 10.4744 11.3168 10.4098 11.1742 10.2262L11.1205 10.1403L11.018 9.95377C10.9816 9.8936 10.9434 9.83515 10.9027 9.77897L10.7738 9.61491C10.0992 8.83195 8.97855 8.52172 7.96327 8.92155C6.67866 9.42757 6.04713 10.8791 6.55311 12.1637L7.83631 15.4206C8.34249 16.7049 9.794 17.3357 11.0785 16.8298C12.3629 16.3236 12.9937 14.8721 12.4877 13.5876L12.3969 13.3551C12.2957 13.0983 12.4213 12.808 12.6781 12.7067C12.935 12.6055 13.2253 12.732 13.3265 12.9889L13.4183 13.2214C14.1268 15.0198 13.2432 17.052 11.4447 17.7604C9.64625 18.4688 7.61412 17.5852 6.90565 15.7868L5.62245 12.5299C4.91434 10.7317 5.79792 8.69938 7.59608 7.99088ZM8.55506 2.23991C10.3536 1.53146 12.3857 2.41505 13.0941 4.21354L14.3773 7.4694C15.0857 9.26779 14.202 11.2999 12.4037 12.0085C10.9807 12.569 9.41236 12.1332 8.46815 11.0368L8.28749 10.8092C8.17297 10.6512 8.07027 10.481 7.98182 10.3014C7.86013 10.0539 7.96206 9.75458 8.20936 9.63249C8.4571 9.5105 8.7573 9.61229 8.87928 9.86002C8.9425 9.98839 9.0156 10.1089 9.09706 10.2214L9.22596 10.3844C9.90056 11.1677 11.022 11.4788 12.0375 11.0788C13.3218 10.5727 13.9524 9.12105 13.4467 7.83659L12.1644 4.57975C11.6584 3.29511 10.2059 2.66356 8.92128 3.1696C7.63695 3.67569 7.00633 5.12732 7.5121 6.41178L7.60389 6.64518C7.70479 6.902 7.57845 7.19247 7.32167 7.29362C7.06479 7.39475 6.77446 7.26823 6.67323 7.01139L6.58143 6.77897C5.87303 4.98058 6.75677 2.94846 8.55506 2.23991Z" fill="currentColor"/></svg>`;

 // Process each H2 and build ToC
 h2Elements.forEach((h2) => {
 const headingText = h2.textContent;
 const baseSlug = textToSlug(headingText);
 const slug = getUniqueSlug(baseSlug);
 
 // Add anchor span
 const anchorSpan = document.createElement('span');
 anchorSpan.id = slug;
 addClass(anchorSpan, 'anchor');
 h2.prepend(anchorSpan);
 
 // Add anchor link box
 const anchorLinkBox = document.createElement('button');
 anchorLinkBox.type = 'button';
 addClass(anchorLinkBox, 'anchor-link-box');
 anchorLinkBox.innerHTML = anchorLinkSVG;
 h2.prepend(anchorLinkBox);
 
 // Initialize copy functionality
 copyAnchorToClipboard(anchorLinkBox, anchorSpan);
 
 // Create ToC item
 const listItem = document.createElement('li');
 addClass(listItem, 'tutorial_post_toc_item');
 
 const link = document.createElement('a');
 link.href = `#${slug}`;
 
 const textDiv = document.createElement('div');
 textDiv.textContent = headingText;
 
 link.appendChild(textDiv);
 listItem.appendChild(link);
 tocList.appendChild(listItem);
 
 tocItems.push({
 element: listItem,
 target: h2
 });
 });
 
 tocContainer.appendChild(tocList);
 
 // Configuration
 const headerHeight = 134;
 const activationOffset = 100;
 
 // State
 let currentActive = 0;
 let ranges = [];
 let frameRequested = false;
 
 // Calculate activation ranges using getBoundingClientRect for reliability
 // (offsetTop can be relative to offsetParent, not document)
 function calculateRanges() {
 const scrollY = window.scrollY;
 
 ranges = tocItems.map((item, index) => {
 const rect = item.target.getBoundingClientRect();
 const absoluteTop = rect.top + scrollY;
 const activationPoint = absoluteTop - headerHeight - activationOffset;
 
 const nextAbsoluteTop = index < tocItems.length - 1
 ? tocItems[index + 1].target.getBoundingClientRect().top + scrollY
 : Infinity;
 const nextActivation = nextAbsoluteTop === Infinity 
 ? Infinity 
 : nextAbsoluteTop - headerHeight - activationOffset;
 
 return {
 index: index,
 start: Math.max(0, activationPoint),
 end: nextActivation
 };
 });
 }
 
 // Update active section
 function updateActiveSection() {
 if (ranges.length === 0) return;
 
 const scrollPosition = window.scrollY;
 let newActive = 0;
 
 // Find current range
 if (scrollPosition < ranges[0].start) {
 newActive = 0;
 } else {
 for (let i = 0; i < ranges.length; i++) {
 if (scrollPosition >= ranges[i].start && scrollPosition < ranges[i].end) {
 newActive = i;
 break;
 }
 }
 }
 
 // Special case: if near bottom of page, activate last item
 const scrollBottom = scrollPosition + window.innerHeight;
 const documentHeight = document.documentElement.scrollHeight;
 if (documentHeight - scrollBottom < 100) {
 newActive = tocItems.length - 1;
 }
 
 // Update classes if changed
 if (newActive !== currentActive) {
 tocItems.forEach(item => removeClass(item.element, 'active'));
 currentActive = newActive;
 if (tocItems[currentActive]) {
 addClass(tocItems[currentActive].element, 'active');
 }
 }
 
 frameRequested = false;
 }
 
 // Scroll handler
 function handleScroll() {
 if (!frameRequested) {
 frameRequested = true;
 window.requestAnimationFrame(updateActiveSection);
 }
 }
 
 // Recalculate on resize (debounced)
 const handleResize = debounce(() => {
 calculateRanges();
 updateActiveSection();
 }, 250);
 
 // Smooth scroll behavior for ToC links
 tocItems.forEach(item => {
 item.element.querySelector('a').addEventListener('click', function(e) {
 e.preventDefault();
 const targetId = this.getAttribute('href').substring(1);
 const targetElement = document.getElementById(targetId);
 
 if (targetElement) {
 const scrollTo = targetElement.parentElement.offsetTop - headerHeight - 20;
 window.scrollTo({
 top: scrollTo,
 behavior: 'smooth'
 });
 }
 });
 });
 
 // Initialize
 calculateRanges();
 addClass(tocItems[0].element, 'active');
 
 // Handle hash on initial page load
 if (window.location.hash) {
 const hash = window.location.hash.substring(1);
 const targetIndex = tocItems.findIndex(item => 
 item.target.querySelector('.anchor')?.id === hash
 );
 if (targetIndex !== -1) {
 tocItems.forEach(item => removeClass(item.element, 'active'));
 addClass(tocItems[targetIndex].element, 'active');
 currentActive = targetIndex;
 }
 }
 
 // Re-check after browser might restore scroll position
 requestAnimationFrame(() => {
 requestAnimationFrame(() => {
 calculateRanges();
 updateActiveSection();
 });
 });
 
 // Event listeners
 window.addEventListener('scroll', handleScroll, { passive: true });
 window.addEventListener('resize', handleResize);
 
 // Visual Viewport API for mobile viewport changes (keyboard, browser chrome)
 if (window.visualViewport) {
 window.visualViewport.addEventListener('resize', handleResize);
 window.visualViewport.addEventListener('scroll', handleResize);
 }
 
 // Browser back/forward navigation with hash changes
 window.addEventListener('popstate', () => {
 calculateRanges();
 updateActiveSection();
 });
 
 // Handle dynamic content changes (if Webflow adds/removes content)
 const observer = new MutationObserver(debounce(() => {
 calculateRanges();
 updateActiveSection();
 }, 500));
 
 observer.observe(tutorialContent, {
 childList: true,
 subtree: true,
 attributes: false
 });
 
 // Recalculate after images load (affects layout positions)
 const images = tutorialContent.querySelectorAll('img');
 images.forEach(img => {
 if (!img.complete) {
 img.addEventListener('load', handleResize, { once: true });
 img.addEventListener('error', handleResize, { once: true });
 }
 });
 
 // Recalculate after fonts load
 if (document.fonts && document.fonts.ready) {
 document.fonts.ready.then(handleResize);
 }
});
How to use Claude in Excel for accounting: Revenue model validationUse Claude to validate ASC 606 revenue models, surface reconciliation issues, and build financial visualizationsCategoryFinanceProductClaude.aiReading timeWatch time3min8minShareCopy linkhttps://claude.com/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validationClaude in Excel works directly inside your spreadsheet through a sidebar, reading your data and making changes through conversation. In this tutorial, you'll see how an accountant uses Claude to validate an ASC 606 revenue recognition model—the kind of multi-tab workbook you might inherit during an audit or acquire in a transaction.What you'll learnUnderstand workbooks you didn't build — Ask Claude to explain how tabs connect. It reads every sheet first, then maps the structure—how schedules tie together, where data flows, what feeds into what.Surface errors and inconsistencies — Claude catches reconciliation gaps, duplicate entries, and missing data across multiple sheets. Instead of clicking through tabs yourself, you see everything it found upfront—and choose what to tackle first.Fix issues with confirmation — When Claude finds a problem, it shows you what's wrong, explains the recommended fix, and waits for your go-ahead. You stay in control of what changes.Add columns and formatting through conversation  — Describe what you need—status indicators, legends, new calculations—and Claude builds it. It learns patterns from your existing data and applies them consistently.Create charts by describing them — Tell Claude what visualization you need. It creates helper tables when necessary, builds the chart, and will rebuild if the first version isn't right.In this videoFollow along with the video, or copy these prompts to try in your own workbook.0:00 — Get oriented in an unfamiliar modelAsk Claude to explain a workbook you've inherited or need to audit. Claude reads every tab before responding, giving it full context for follow-up questions."Walk me through this model. What's on each tab and how does everything tie together?"1:13 — Let Claude surface issues for youAfter reading the workbook, Claude proactively identifies problems: reconciliation gaps, duplicate entries, missing data. You choose which to tackle first."Yes, please look at the reconciliation issue first."2:17 — Fix data with confirmationClaude shows you what it found and what it recommends. It won't make changes until you say so."Yes, go ahead."3:09 — Add columns through conversationDescribe what you want—status indicators, legends, new calculations—and Claude adds them."Add a check mark column showing testing status for each contract. Use ✓ for tested, IP for in progress, and NP for not yet started. Add a legend at the bottom."4:24 — Create charts by describing themTell Claude what visualization you need. It creates helper tables when necessary and will rebuild if the first version isn't right."Create a waterfall chart showing the Q3 deferred revenue rollforward—beginning balance, bookings, revenue recognized, adjustments, and ending balance."6:11 — Return to earlier issuesClaude remembers everything from your conversation. Circle back to issues it flagged earlier without re-explaining."Let's go back to the issues you identified—a missing journal entry and one other I think?"What to noticeClaude reads before it answers. When you ask about the model, Claude doesn't guess—it reads all six sheets first, then explains how they connect. This prevents errors from incomplete context and gives Claude the baseline it needs for follow-up questions.Issues surface together. Instead of discovering problems one at a time as you click through tabs, Claude presents everything it found upfront: the reconciliation gap, the duplicate, the missing entry, the flagged items. You decide what to tackle first.Changes require confirmation. Claude shows the math, explains what will change, and waits for your "yes, go ahead" before modifying anything. You see exactly what's happening and can verify the logic.Context carries through the conversation. When you say "let's go back to the issues you identified," Claude remembers what it flagged earlier. You don't need to re-explain or re-read the model.Claude learns patterns from your data. When adding September journal entries, Claude analyzed the existing July and August entries, identified that revenue splits 80% Platform / 12% Support / 8% Services, and applied that same logic. The new entries follow your established pattern.Next stepsThis tutorial shows one use case: validating an ASC 606 revenue model with reconciliation issues and missing entries. The same approach works for any multi-sheet model where you need to understand the structure, catch problems, or extend what's already built—budgets, forecasts, audit workpapers.Get started:Install Claude in Excel from Microsoft AppSourceOpen it with Ctrl+Option+C (Mac) or Ctrl+Alt+C (Windows)Start with "Walk me through this model" on any spreadsheet you've inheritedLearn more:Claude in Excel help articleWhat is the Max plan?What you'll learnIn this videoWhat to noticeNext stepsRelated tutorialsGetting started with Claude in ExcelGetting started with Claude in ExcelGetting started with Claude in ExcelTutorialTutorialTutorialHow to use Claude in Excel for HR: Headcount planningHow to use Claude in Excel for HR: Headcount planningHow to use Claude in Excel for HR: Headcount planningTutorialTutorialTutorialPrompting strategies for financial analysisPrompting strategies for financial analysisPrompting strategies for financial analysisTutorialTutorialTutorialClaude for financial services overviewClaude for financial services overviewClaude for financial services overviewTutorialTutorialTutorial
 @container (width < 52em) {
 .footer_layout {
 display: flex;
 column-gap: var(--_spacing---space--4rem);
 row-gap: var(--_spacing---space--4rem);
 }
 .footer_content_wrap.u-column-custom {
 display: contents;
 }
 }

 .footer_link {
 opacity: 1;
 transition: opacity 0.3s ease;
 }
 .footer_links_list:has(.footer_link:hover) .footer_link:not(:hover) {
 opacity: 0.4;
 }
HomepageHomepageNextNextThank you! Your submission has been received!Oops! Something went wrong while submitting the form.
 (function () {
 const ROOT_SEL = "[data-prompt-scope]";
 const TRIGGER_SEL = "[data-prompt-trigger]";
 const MENU_ATTR = "data-prompt-menu";
 const CLOSE_SEL = "[data-prompt-menu-close]";
 const ACTION_SEL = "a, button, [data-prompt-menu-action]";
 const ITEM_SEL = "[data-prompt-item], li, .menu-item, .w-dyn-item";

 // ---------- Claude helper ----------
 function buildClaudeUrl(text) {
 const url = new URL("https://claude.ai/new");
 url.searchParams.set("q", text || "");
 return url.toString();
 }
 function openClaude(text) {
 const q = (text || "").trim();
 if (!q) return;
 window.open(buildClaudeUrl(q), "_blank", "noopener");
 }

 // ---------- Utilities ----------
 let uid = 0;
 function makeId(prefix = "prompt-menu") {
 uid += 1;
 return `${prefix}-${Date.now().toString(36)}-${uid}`;
 }

 // Limit queries to elements that belong to THIS scope (ignore nested scopes)
 function qsaInScope(root, sel) {
 return Array.from(root.querySelectorAll(sel)).filter(
 (el) => el.closest(ROOT_SEL) === root
 );
 }

 // Lightweight shield to stop click-through during the brief close animation
 function deployClickShield(ms = 300) {
 const sh = document.createElement("div");
 sh.style.cssText =
 "position:fixed;inset:0;z-index:2147483647;pointer-events:auto;background:transparent";
 document.body.appendChild(sh);
 setTimeout(() => {
 sh.remove();
 }, ms);
 }

 // Pairing: find which menu a trigger controls (no manual ids needed)
 function resolveMenuForTrigger(root, trigger) {
 // 1) explicit data-prompt-trigger="x" -> [data-prompt-menu="x"]
 const explicit = trigger.getAttribute("data-prompt-trigger");
 if (explicit) {
 const m = qsaInScope(root, `[${MENU_ATTR}="${explicit}"]`)[0];
 if (m) return m;
 }
 // 2) aria-controls
 const ctrl = trigger.getAttribute("aria-controls");
 if (ctrl) {
 const m = qsaInScope(root, `#${ctrl.replace(/(["'\\])/g, "\\$1")}`)[0];
 if (m) return m;
 }
 // 3) nearest following sibling with [data-prompt-menu]
 let sib = trigger.nextElementSibling;
 while (sib && sib !== root) {
 if (
 sib.hasAttribute &&
 sib.hasAttribute(MENU_ATTR) &&
 sib.closest(ROOT_SEL) === root
 )
 return sib;
 sib = sib.nextElementSibling;
 }
 // 4) first menu in this root
 return qsaInScope(root, `[${MENU_ATTR}]`)[0] || null;
 }

 function ensurePairing(trigger, menu) {
 if (!menu.id) menu.id = makeId();
 trigger.setAttribute("aria-controls", menu.id);
 if (trigger.tagName === "BUTTON" && !trigger.hasAttribute("type"))
 trigger.type = "button";
 }

 // ---------- Animations (GSAP) ----------
 function revealMenu(menu) {
 return new Promise((resolve) => {
 gsap.set(menu, {
 visibility: "visible",
 pointerEvents: "auto",
 willChange: "transform, opacity",
 });
 gsap.killTweensOf(menu);
 gsap.fromTo(
 menu,
 { opacity: 0, scale: 0.96 },
 {
 opacity: 1,
 scale: 1,
 duration: 0.28,
 ease: "power3.out",
 clearProps: "willChange",
 onComplete: resolve,
 }
 );
 });
 }
 function hideMenu(menu) {
 return new Promise((resolve) => {
 gsap.killTweensOf(menu);
 gsap.to(menu, {
 opacity: 0,
 duration: 0.2,
 ease: "power2.out",
 onComplete: () => {
 gsap.set(menu, {
 visibility: "hidden",
 pointerEvents: "none",
 clearProps: "opacity,scale,willChange",
 });
 resolve();
 },
 });
 });
 }

 // ---------- Per-scope controller ----------
 const stateMap = new WeakMap(); // root -> { openMenuEl, openTrigger, isAnimating }

 function getState(root) {
 let s = stateMap.get(root);
 if (!s) {
 s = { openMenuEl: null, openTrigger: null, isAnimating: false };
 stateMap.set(root, s);
 }
 return s;
 }

 function setTriggersInteractive(root, enabled) {
 qsaInScope(root, TRIGGER_SEL).forEach((el) => {
 el.style.pointerEvents = enabled ? "auto" : "none";
 });
 }

 // ---------- Button fade animations ----------
 function fadeOutButtons(root) {
 return new Promise((resolve) => {
 const buttons = qsaInScope(root, TRIGGER_SEL);
 if (buttons.length === 0) {
 resolve();
 return;
 }

 gsap.killTweensOf(buttons);
 gsap.to(buttons, {
 autoAlpha: 0,
 duration: 0.2,
 ease: "power2.out",
 onComplete: resolve,
 });
 });
 }

 function fadeInButtons(root) {
 return new Promise((resolve) => {
 const buttons = qsaInScope(root, TRIGGER_SEL);
 if (buttons.length === 0) {
 resolve();
 return;
 }

 gsap.killTweensOf(buttons);
 gsap.to(buttons, {
 autoAlpha: 1,
 duration: 0.2,
 ease: "power2.out",
 onComplete: resolve,
 });
 });
 }

 async function openMenuIn(root, menu, trigger) {
 const s = getState(root);
 if (s.isAnimating || s.openMenuEl === menu) return;
 s.isAnimating = true;

 // close any currently open in THIS scope only
 if (s.openMenuEl && s.openMenuEl !== menu) {
 await hideMenu(s.openMenuEl);
 if (s.openTrigger) s.openTrigger.setAttribute("aria-expanded", "false");
 }

 // Fade out buttons when opening menu
 await fadeOutButtons(root);

 await revealMenu(menu);
 s.openMenuEl = menu;
 s.openTrigger = trigger || null;
 if (s.openTrigger) s.openTrigger.setAttribute("aria-expanded", "true");

 // Disable only this scope's triggers while open
 setTriggersInteractive(root, false);

 s.isAnimating = false;
 }

 async function closeMenuIn(root) {
 const s = getState(root);
 if (!s.openMenuEl || s.isAnimating) return;
 s.isAnimating = true;

 deployClickShield(280); // prevent click-through during closing
 await hideMenu(s.openMenuEl);

 if (s.openTrigger) s.openTrigger.setAttribute("aria-expanded", "false");
 s.openMenuEl = null;
 s.openTrigger = null;

 // Re-enable only this scope's triggers
 setTriggersInteractive(root, true);

 // Fade in buttons when closing menu
 await fadeInButtons(root);

 s.isAnimating = false;
 }

 // ---------- Initializer ----------
 const initedRoots = new WeakSet();

 function initScope(root) {
 if (!root || initedRoots.has(root)) return;
 initedRoots.add(root);

 if (!window.gsap) {
 console.warn("GSAP is required for prompt menus.");
 return;
 }

 // Normalize ALL menus in this scope to hidden on init (prevents “open on load” bugs)
 qsaInScope(root, `[${MENU_ATTR}]`).forEach((menu) => {
 if (menu.dataset.pmMenuInit) return;
 menu.dataset.pmMenuInit = "true";
 gsap.set(menu, {
 visibility: "hidden",
 opacity: 0,
 scale: 1,
 pointerEvents: "none",
 });

 // Optional close button
 const closer = menu.querySelector(CLOSE_SEL);
 if (closer) {
 if (closer.tagName === "BUTTON" && !closer.hasAttribute("type"))
 closer.type = "button";
 closer.addEventListener("click", (e) => {
 e.preventDefault();
 e.stopPropagation();
 closeMenuIn(root);
 });
 }

 // Menu item -> Claude
 menu.addEventListener("click", (e) => {
 const target = e.target.closest(ACTION_SEL);
 if (!target || !menu.contains(target)) return;

 const container = target.closest(ITEM_SEL) || target;
 const hiddenP = container.querySelector("[data-prompt-menu-text]");
 if (!hiddenP) return;

 e.preventDefault();
 e.stopPropagation();

 const text = hiddenP.textContent || hiddenP.innerText || "";
 openClaude(text);

 // close after action
 closeMenuIn(root);
 });
 });

 // Bind triggers (auto-wire)
 qsaInScope(root, TRIGGER_SEL).forEach((trigger) => {
 if (trigger.dataset.pmTrigInit) return;
 trigger.dataset.pmTrigInit = "true";

 const menu = resolveMenuForTrigger(root, trigger);
 if (menu) ensurePairing(trigger, menu);

 trigger.setAttribute("aria-expanded", "false");

 trigger.addEventListener("click", async (e) => {
 e.preventDefault();

 const targetMenu = resolveMenuForTrigger(root, trigger);
 if (!targetMenu) return;

 const s = getState(root);
 if (s.openMenuEl === targetMenu) {
 await closeMenuIn(root); // toggle close
 return;
 }
 await openMenuIn(root, targetMenu, trigger);
 });
 });

 // Outside click (this scope only)
 document.addEventListener("click", (e) => {
 const s = getState(root);
 if (!s.openMenuEl) return;
 const insideMenu = s.openMenuEl.contains(e.target);
 const onTrigger =
 !!e.target.closest(TRIGGER_SEL) && root.contains(e.target);
 if (!insideMenu && !onTrigger) closeMenuIn(root);
 });

 // ESC (this scope only)
 document.addEventListener("keydown", (e) => {
 if (e.key === "Escape") closeMenuIn(root);
 });
 }

 // ---------- Boot + observe ----------
 function boot(container = document) {
 const roots = container.querySelectorAll
 ? container.querySelectorAll(ROOT_SEL)
 : [];
 roots.forEach(initScope);
 }

 if (document.readyState === "loading") {
 document.addEventListener("DOMContentLoaded", () => boot(), {
 once: true,
 });
 } else {
 boot();
 }

 const mo = new MutationObserver((muts) => {
 for (const m of muts) {
 for (const node of m.addedNodes || []) {
 if (node.nodeType !== 1) continue;
 if (node.matches && node.matches(ROOT_SEL)) initScope(node);
 if (node.querySelectorAll) {
 node.querySelectorAll(ROOT_SEL).forEach(initScope);
 }
 }
 }
 });
 mo.observe(document.documentElement, { childList: true, subtree: true });
 })();

(function () {
 // ---------- Claude helper ----------
 function buildClaudeUrl(text) {
 const url = new URL('https://claude.ai/new');
 url.searchParams.set('q', text || '');
 return url.toString();
 }

 // ---------- Auto-grow helpers ----------
 function sizeTextarea(el) {
 // Ensure UA defaults don't force a starting height
 el.setAttribute('rows', el.getAttribute('data-min-rows') || '1');
 el.style.minHeight = '0px';
 el.style.height = 'auto'; // allow shrink
 el.style.height = el.scrollHeight + 'px'; // fit content
 }

 function initAutogrow(root = document) {
 root.querySelectorAll('textarea[data-autogrow]').forEach((el) => {
 if (el.dataset.autogrowInit) return;
 el.dataset.autogrowInit = 'true';

 // Respect your existing pattern for default text
 const preset = el.getAttribute('data-default-text');
 if (preset != null && !el.value) el.value = preset;

 // Initial sizing
 sizeTextarea(el);

 // Resize as you type
 el.addEventListener('input', () => sizeTextarea(el));

 // In case fonts/styles load late and change line-height
 window.addEventListener('load', () => sizeTextarea(el), { once: true });
 });
 }

 // ---------- Claude form initializer ----------
 function initClaudeForms(root = document) {
 root.querySelectorAll('form[data-claude-form]').forEach((form) => {
 if (form.dataset.claudeInit) return;
 form.dataset.claudeInit = 'true';

 const textarea = form.querySelector('[data-claude-textarea], textarea');
 const trigger = form.querySelector('[data-claude-button], button[type="button"], a[data-claude-button]');

 if (!textarea || !trigger) {
 console.warn('Claude form: missing textarea or trigger in', form);
 return;
 }

 // If the trigger is a <button> but has no type, force "button" so it won't submit
 if (trigger.tagName === 'BUTTON' && !trigger.hasAttribute('type')) {
 trigger.type = 'button';
 }

 // Keep <a> from navigating away while still opening Claude
 if (trigger.tagName === 'A') {
 trigger.addEventListener('click', (e) => e.preventDefault());
 }

 // Optional: support data-default-text on the textarea
 const preset = textarea.getAttribute('data-default-text');
 if (preset != null && !textarea.value) textarea.value = preset;

 // Click opens Claude; submission is optional
 trigger.addEventListener('click', () => {
 const text = (textarea.value || '').trim();
 if (!text) {
 textarea.focus();
 return;
 }

 window.open(buildClaudeUrl(text), '_blank', 'noopener');

 const mode = form.getAttribute('data-claude-mode') || 'intercept';
 if (mode === 'also') {
 // Submit after opening Claude
 form.submit();
 }
 // intercept mode: do nothing (no submit)
 });

 // (Optional) Keep an <a data-claude-button> href in sync for right-click/open-in-new-tab UX
 if (trigger.tagName === 'A') {
 const syncHref = () => trigger.setAttribute('href', buildClaudeUrl((textarea.value || '').trim()));
 syncHref();
 textarea.addEventListener('input', syncHref);
 textarea.addEventListener('change', syncHref);
 }
 });
 }

 // ---------- Boot ----------
 function initAll(root = document) {
 initAutogrow(root);
 initClaudeForms(root);
 }

 if (document.readyState === 'loading') {
 document.addEventListener('DOMContentLoaded', () => initAll(), { once: true });
 } else {
 initAll();
 }

 // Re-init if content is injected later (Webflow CMS / IX / tabs)
 const mo = new MutationObserver((muts) => {
 for (const m of muts) {
 for (const node of m.addedNodes || []) {
 if (node.nodeType === 1) initAll(node);
 }
 }
 });
 mo.observe(document.documentElement, { childList: true, subtree: true });
})();

 .prompt_menu_item {
 transition: border-color 0.2s ease, color 0.2s ease;
 }
 .prompt_menu_item_base, .prompt_menu_item_icon {
 transition: opacity 0.2s ease;
 }
 .prompt_menu_list .prompt_menu_item:first-child {
 border-color: transparent;
 }
 .prompt_menu_item:hover {
 border-color: transparent;
 color: var(--_theme---foreground-primary);
 }
 .prompt_menu_item:hover .prompt_menu_item_base {
 opacity: 1;
 }
 .prompt_menu_item:hover .prompt_menu_item_icon {
 opacity: 1;
 }
 .prompt_menu_item:hover + .prompt_menu_item {
 border-top-color: transparent;
 }

 .button_prompt_icon {
 transition: color 0.3s ease;
 }
 .button_prompt_wrap:hover .button_prompt_icon {
 color: var(--_button-style---icon-hover); 
 }
 .button_prompt_wrap:focus-within .button_prompt_icon {
 color: var(--_button-style---text-hover) !important;
 }
 .button_prompt_wrap:focus-within {
 color: var(--_button-style---text-hover) !important;
 }

WriteButton TextButton TextLearnButton TextButton TextCodeButton TextButton TextWriteHelp me develop a unique voice for an audienceHi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!Improve my writing styleHi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!Brainstorm creative ideasHi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!LearnExplain a complex topic simplyHi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!Help me make sense of these ideasHi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!Prepare for an exam or interviewHi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!CodeExplain a programming conceptHi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!Look over my code and give me tipsHi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!Vibe code with meHi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!MoreWrite case studiesThis is another testWrite grant proposalsHi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational. Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!Write video scriptsthis is a testAnthropicAnthropic© 2026 Anthropic PBCProductsClaudeClaudeClaudeClaude CodeClaude CodeClaude CodeCoworkCoworkCoworkMax planMax planMax planTeam planTeam planTeam planEnterprise planEnterprise planEnterprise planDownload appDownload appDownload appPricingPricingPricingLog inLog inLog inFeaturesClaude in ChromeClaude in ChromeClaude in ChromeClaude in SlackClaude in SlackClaude in SlackClaude in ExcelClaude in ExcelClaude in ExcelSkillsSkillsSkillsModelsOpusOpusOpusSonnetSonnetSonnetHaikuHaikuHaikuSolutionsAI agentsAI agentsAI agentsCode modernizationCode modernizationCode modernizationCodingCodingCodingCustomer supportCustomer supportCustomer supportEducationEducationEducationFinancial servicesFinancial servicesFinancial servicesGovernmentGovernmentGovernmentHealthcareHealthcareHealthcareLife sciencesLife sciencesLife sciencesNonprofitsNonprofitsNonprofitsClaude Developer PlatformOverviewOverviewOverviewDeveloper docsDeveloper docsDeveloper docsPricingPricingPricingRegional ComplianceRegional ComplianceRegional ComplianceAmazon BedrockAmazon BedrockAmazon BedrockGoogle Cloud’s Vertex AIGoogle Cloud’s Vertex AIGoogle Cloud’s Vertex AIConsole loginConsole loginConsole loginLearnBlogBlogBlogClaude partner networkClaude partner networkClaude partner networkCoursesCoursesCoursesConnectorsConnectorsConnectorsCustomer storiesCustomer storiesCustomer storiesEngineering at AnthropicEngineering at AnthropicEngineering at AnthropicEventsEventsEventsPluginsPluginsPluginsPowered by ClaudePowered by ClaudePowered by ClaudeService partnersService partnersService partnersStartups programStartups programStartups programTutorialsTutorialsTutorialsUse casesUse casesUse casesCompanyAnthropicAnthropicAnthropicCareersCareersCareersEconomic FuturesEconomic FuturesEconomic FuturesResearchResearchResearchNewsNewsNewsResponsible Scaling PolicyResponsible Scaling PolicyResponsible Scaling PolicySecurity and complianceSecurity and complianceSecurity and complianceTransparencyTransparencyTransparencyHelp and securityAvailabilityAvailabilityAvailabilityStatusStatusStatusSupport centerSupport centerSupport centerTerms and policiesPrivacy choices
 /* Dialog styling */
 dialog#consent-container {
 margin: 0;
 padding: 8px;
 opacity: 0;
 transform: translateY(16px);
 transition: opacity 0.3s ease-out, transform 0.3s ease-out;
 }

 dialog#consent-container.show {
 opacity: 1;
 transform: translateY(0);
 }

 dialog#consent-container::backdrop {
 background: transparent;
 }

 dialog button span {
 display: inline !important;
 }

 /* Toggle switch styling */
 .toggle_switch {
 position: relative;
 display: inline-block;
 width: 36px;
 height: 24px;
 }

 .toggle_switch input {
 opacity: 0;
 width: 0;
 height: 0;
 }

 .toggle_slider {
 position: absolute;
 cursor: pointer;
 top: 0;
 left: 0;
 right: 0;
 bottom: 0;
 background-color: #87867f;
 transition: .4s;
 border-radius: 24px;
 }

 .toggle_slider:before {
 position: absolute;
 content: "";
 height: 18px;
 width: 18px;
 left: 3px;
 bottom: 3px;
 background-color: white;
 transition: .4s;
 border-radius: 50%;
 }

 input:checked + .toggle_slider {
 background-color: #d97757;
 }

 input:checked + .toggle_slider:before {
 transform: translateX(12px);
 }

 input:disabled + .toggle_slider {
 cursor: not-allowed;
 opacity: 0.5;
 }

 @media only screen and (max-width: 501px) {
 dialog#consent-container {
 left: 8px !important;
 bottom: 8px !important;
 right: 8px !important;
 }
 #consent-banner {
 padding: 24px 16px 16px !important;
 }
 #simple-options {
 grid-template-columns: repeat(3, 1fr) !important;
 grid-template-rows: auto auto !important;
 }
 #customize-btn {
 grid-column: span 1 !important;
 }
 dialog button span {
 display: none !important;
 }

 
 Cookie settings
 
 We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy here.
 

 
 
 Customize cookie settings
 
 
 Reject all cookies
 
 
 Accept all cookies
 
 

 
 
 
 
 
 Necessary
 Enables security and basic functionality.
 
 
 Required
 
 
 
 
 
 

 
 
 
 Analytics
 Enables tracking of site performance.
 
 
 Off
 
 
 
 
 
 

 
 
 
 Marketing
 Enables ads personalization and tracking.
 
 
 Off
 
 
 
 
 
 
 

 
 Save preferences
 
 
 
Privacy policyPrivacy policyPrivacy policyResponsible disclosure policyResponsible disclosure policyResponsible disclosure policyTerms of service: CommercialTerms of service: CommercialTerms of service: CommercialTerms of service: ConsumerTerms of service: ConsumerTerms of service: ConsumerUsage policyUsage policyUsage policyx.comx.comLinkedInLinkedInYouTubeYouTubeInstagramInstagramEnglish (US)

 function initDynamicCurrentYear() { 
 const currentYear = new Date().getFullYear();
 const currentYearElements = document.querySelectorAll('[data-current-year]');
 currentYearElements.forEach(currentYearElement => {
 currentYearElement.textContent = currentYear;
 });
 }

 // Initialize Dynamic Current Year
 document.addEventListener('DOMContentLoaded', () => {
 initDynamicCurrentYear();
 });
gsap.registerPlugin(ScrollTrigger,SplitText,TextPlugin,Flip,Draggable,InertiaPlugin);

 document.addEventListener('DOMContentLoaded', function() {
 const contentElement = document.querySelector('[data-readtime="content"]');
 const minutesElement = document.querySelector('[data-readtime="minutes"]');

 if (!contentElement || !minutesElement) return;

 const text = contentElement.innerText || contentElement.textContent;
 const wordCount = text.trim().split(/\s+/).length;
 const wordsPerMinute = 250;
 const minutes = Math.round(wordCount / wordsPerMinute);

 minutesElement.textContent = minutes || 1; // minimum 1 minute
 });
 
 // Hide all empty paragraph tags from the main content RTF
 document.querySelectorAll('#tutorial_content p').forEach(p => {
 if (p.textContent.trim() === '' || /^[\u200B-\u200D\uFEFF]+$/.test(p.textContent)) {
 p.remove();
 }
 });

 
 
 
 ×