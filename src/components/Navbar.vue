<template>
    <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">

            <!-- DESKTOP MODE -->
            <a @click="resetNavigation()" class="is-hidden-mobile">
                <img src="../assets/website-logo.png">
            </a>
            <!-- MOBILE MODE -->
            <a @click="resetNavigation()" class="is-hidden-tablet">
                <img style="width:205px;margin-left:4%" src="../assets/website-logo.png">
            </a>
            <!-- ------------ -->

            <a @click="this.phoneMenu()" style="height:67px" role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navMenu">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>

        </div>

        <!-- MOBILE MODE -->
        <div class="navbar-menu" id="navMenu" ref="phoneMenuSlide" v-if="phoneMenuBurger" :class="{ 'is-active' : phoneMenuBurger }">
            <div>
                <p @click="resetNavigation()" class="phone-menu">
                    <svg class="navbar-icon-menu-sandwich" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.09 4.83C9.28891 4.83 9.47967 4.75098 9.62033 4.61033C9.76098 4.46968 9.84 4.27891 9.84 4.08C9.84 3.88109 9.76098 3.69032 9.62033 3.54967C9.47967 3.40902 9.28891 3.33 9.09 3.33H5.62C5.42189 3.33259 5.23262 3.41244 5.09253 3.55254C4.95243 3.69263 4.87259 3.88189 4.87 4.08V20.2C4.87259 20.3981 4.95243 20.5874 5.09253 20.7275C5.23262 20.8676 5.42189 20.9474 5.62 20.95H9.09C9.28891 20.95 9.47967 20.871 9.62033 20.7303C9.76098 20.5897 9.84 20.3989 9.84 20.2C9.84 20.0011 9.76098 19.8103 9.62033 19.6697C9.47967 19.529 9.28891 19.45 9.09 19.45H6.37V4.83H9.09Z" fill="#A6A6EF"/>
                        <path d="M17.78 3.3L12.78 2.05C12.5173 1.98257 12.2426 1.97641 11.9771 2.03201C11.7116 2.08761 11.4625 2.20348 11.2489 2.37067C11.0353 2.53786 10.863 2.7519 10.7453 2.99627C10.6276 3.24063 10.5676 3.50878 10.57 3.78V20.21C10.5687 20.4446 10.6138 20.6771 10.7026 20.8942C10.7915 21.1114 10.9224 21.3088 11.0878 21.4751C11.2532 21.6415 11.4499 21.7735 11.6665 21.8636C11.8831 21.9536 12.1154 22 12.35 22C12.4987 21.9997 12.6467 21.9795 12.79 21.94L17.79 20.69C18.1675 20.5938 18.5031 20.3763 18.7451 20.0711C18.9872 19.7658 19.1224 19.3895 19.13 19V5C19.124 4.60742 18.9883 4.22785 18.7442 3.92039C18.5 3.61292 18.161 3.3948 17.78 3.3ZM13.62 13.37C13.17 13.37 12.62 13.01 12.62 12C12.62 10.99 13.14 10.62 13.62 10.62C14.1 10.62 14.62 10.98 14.62 12C14.62 13.02 14.08 13.37 13.62 13.37Z" fill="#A6A6EF"/>
                    </svg>
                    Accueil
                </p>
                <div class="phone-menu">
                    <p class="phone-menu">
                        <svg class="navbar-icon-menu-sandwich" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3.78003 12.75H6.11002V20.22C6.11002 21.2 6.91005 22 7.89005 22H8.92004C9.90004 22 10.69 21.2 10.69 20.22V12.75H17.48C17.69 12.75 17.9 12.66 18.04 12.5L20.78 9.41C21.04 9.13 21.04 8.7 20.78 8.42L18.04 5.33C17.9 5.17 17.69 5.08 17.48 5.08H10.69V3.78C10.69 2.8 9.90004 2 8.92004 2H7.89005C6.91005 2 6.11002 2.8 6.11002 3.78V5.08H3.78003C3.36003 5.08 3.03003 5.42 3.03003 5.83V12C3.03003 12.41 3.36003 12.75 3.78003 12.75ZM7.61002 3.78C7.61002 3.63 7.74005 3.5 7.89005 3.5H8.92004C9.07004 3.5 9.19003 3.63 9.19003 3.78V5.08H7.61002V3.78ZM7.61002 12.75H9.19003V20.22C9.19003 20.37 9.07004 20.5 8.92004 20.5H7.89005C7.74005 20.5 7.61002 20.37 7.61002 20.22V12.75Z" fill="#A6A6EF"/>
                        </svg> 
                        Catégorie
                    </p>

                    <div class="navbar-dropdown">
                        <template v-if="this.categories.length > 0">
                            <template v-for="(categorie, index) in this.categories" :key="index">
                                <a @click="goToThread(categorie.id)" class="navbar-item navbar-line">
                                    • {{categorie.nom}}
                                </a>
                            </template>
                        </template>
                        <template v-else>
                            <a class="navbar-item">Aucune catégorie pour le moment.</a>
                        </template>
                    </div>
                </div>
                <p @click="getSelection()" class="phone-menu">
                    <svg class="navbar-icon-menu-sandwich" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M11.13 11.17L14.25 9.76L12.87 12.83L9.72 14.32L11.13 11.17Z" fill="#A6A6EF"/>
                        <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM15.7 10.17L14.19 13.49C14.05 13.8 13.8 14.05 13.49 14.19L10.17 15.7C9.98 15.79 9.78 15.83 9.58 15.83C9.21 15.83 8.86 15.69 8.58 15.42C8.16 15 8.05 14.37 8.3 13.83L9.81 10.51C9.95 10.2 10.2 9.95 10.51 9.81L13.83 8.3C14.37 8.05 15 8.16 15.42 8.58C15.84 9 15.95 9.63 15.7 10.17Z" fill="#A6A6EF"/>
                    </svg>
                    Notre sélection
                </p>
                <p @click="getBestOf()" class="phone-menu">
                    <svg class="navbar-icon-menu-sandwich" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19.3 4.05H17.92V2.75C17.9213 2.65114 17.9029 2.55301 17.8656 2.4614C17.8284 2.3698 17.7732 2.28659 17.7033 2.21667C17.6334 2.14676 17.5502 2.09156 17.4586 2.05435C17.367 2.01714 17.2689 1.99865 17.17 2H6.88999C6.69108 2 6.50031 2.07902 6.35966 2.21967C6.21901 2.36032 6.13999 2.55109 6.13999 2.75V4.05H4.70999C4.25541 4.03377 3.81291 4.19826 3.47932 4.50749C3.14573 4.81672 2.94822 5.2455 2.92999 5.7V8.93C2.93116 9.15616 2.98086 9.37944 3.07575 9.58473C3.17063 9.79003 3.30849 9.97257 3.47999 10.12L7.14999 13.38C7.62118 14.053 8.23252 14.6161 8.942 15.0304C9.65149 15.4447 10.4423 15.7004 11.26 15.78V17.39H8.81999C8.37939 17.3929 7.95553 17.5592 7.63042 17.8566C7.30532 18.154 7.10206 18.5614 7.05999 19L6.90999 20C6.8768 20.2521 6.898 20.5084 6.97217 20.7516C7.04635 20.9948 7.17177 21.2193 7.33999 21.41C7.50597 21.5985 7.71078 21.7488 7.94036 21.8507C8.16995 21.9525 8.41886 22.0035 8.66999 22H15.39C15.6418 21.9991 15.8905 21.9448 16.1198 21.8407C16.349 21.7365 16.5536 21.585 16.7199 21.3959C16.8863 21.2069 17.0106 20.9847 17.0847 20.7441C17.1589 20.5035 17.1811 20.2499 17.15 20L17 19C16.94 18.5749 16.7293 18.1855 16.4063 17.9028C16.0832 17.6202 15.6693 17.463 15.24 17.46H12.78V15.8C13.6289 15.7205 14.4491 15.4509 15.1796 15.0112C15.9102 14.5715 16.5323 13.973 17 13.26L20.52 10.13C20.6913 9.9802 20.8288 9.7958 20.9236 9.58896C21.0184 9.38212 21.0683 9.15753 21.07 8.93V5.7C21.0623 5.4754 21.0103 5.25452 20.9171 5.05C20.824 4.84549 20.6914 4.66135 20.527 4.5081C20.3626 4.35486 20.1696 4.23552 19.9591 4.15692C19.7486 4.07831 19.5246 4.04198 19.3 4.05ZM4.42999 8.93V5.7C4.42999 5.65 4.53999 5.55 4.70999 5.55H6.13999V10.14C6.13999 10.26 6.13999 10.37 6.13999 10.48L4.42999 8.93ZM14.43 8.53L13.77 9.18L13.92 10.09C13.9447 10.2281 13.9306 10.3703 13.8794 10.5009C13.8283 10.6315 13.7419 10.7454 13.63 10.83C13.5065 10.9278 13.3569 10.9869 13.2 11C13.081 10.9986 12.9641 10.9676 12.86 10.91L12 10.45L11.18 10.88C11.0568 10.9462 10.9175 10.9765 10.7779 10.9677C10.6383 10.9589 10.5039 10.9112 10.39 10.83C10.2763 10.7466 10.188 10.6333 10.135 10.5026C10.082 10.3719 10.0664 10.229 10.09 10.09L10.25 9.18L9.57999 8.53C9.47948 8.43206 9.40846 8.30789 9.37501 8.17159C9.34157 8.0353 9.34703 7.89235 9.39078 7.75901C9.43454 7.62567 9.51482 7.50727 9.62252 7.41729C9.73021 7.32731 9.86099 7.26935 9.99999 7.25L11 7.11L11.41 6.28C11.4805 6.16411 11.5796 6.06832 11.6978 6.00185C11.816 5.93537 11.9494 5.90046 12.085 5.90046C12.2206 5.90046 12.354 5.93537 12.4722 6.00185C12.5904 6.06832 12.6895 6.16411 12.76 6.28L13.17 7.11L14.09 7.25C14.2275 7.27103 14.3564 7.32986 14.4623 7.41992C14.5683 7.50998 14.6471 7.62773 14.69 7.76C14.7288 7.89781 14.7267 8.0439 14.6841 8.18057C14.6415 8.31724 14.5602 8.43862 14.45 8.53H14.43ZM15.23 18.91C15.2967 18.9096 15.3612 18.9339 15.411 18.9782C15.4609 19.0225 15.4926 19.0837 15.5 19.15L15.65 20.15C15.654 20.1895 15.6499 20.2294 15.6378 20.2673C15.6258 20.3051 15.6061 20.3401 15.58 20.37C15.5552 20.4018 15.5232 20.4274 15.4868 20.4448C15.4503 20.4621 15.4104 20.4708 15.37 20.47H8.66999C8.63104 20.4708 8.59248 20.4621 8.55764 20.4447C8.52279 20.4273 8.49271 20.4016 8.46999 20.37C8.43997 20.3428 8.41768 20.3081 8.40539 20.2694C8.3931 20.2308 8.39124 20.1896 8.39999 20.15L8.53999 19.15C8.55158 19.0837 8.58585 19.0235 8.63693 18.9798C8.68801 18.936 8.75273 18.9113 8.81999 18.91H15.23ZM19.52 9L17.91 10.44C17.91 10.34 17.91 10.24 17.91 10.14V5.55H19.3C19.47 5.55 19.57 5.65 19.57 5.7L19.52 9Z" fill="#A6A6EF"/>
                    </svg>
                    Meilleur de 2022
                </p>
            </div>

            <div class="control has-icons-right" style="margin-top:20%;">
                <input 
                v-on:keyup="inputCompletion()"
                v-model="this.clientInput"
                class="input is-medium search-bar" type="email" placeholder="Recherche ...">
                <span class="icon is-medium is-right search-button">
                    <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10.97 5.91C8.18003 5.91 5.91003 8.18 5.91003 10.97C5.91003 13.76 8.18003 16.04 10.97 16.04C13.77 16.04 16.04 13.76 16.04 10.97C16.04 8.18 13.77 5.91 10.97 5.91Z" fill="grey"/>
                        <path d="M21.78 20.72L17.82 16.76C19.14 15.19 19.94 13.18 19.94 10.97C19.94 6.03 15.92 2 10.97 2C6.03 2 2 6.03 2 10.97C2 15.92 6.03 19.94 10.97 19.94C13.18 19.94 15.2 19.14 16.76 17.82L20.72 21.78C20.87 21.93 21.06 22 21.25 22C21.44 22 21.63 21.93 21.78 21.78C22.07 21.49 22.07 21.01 21.78 20.72ZM10.97 17.54C7.35 17.54 4.41 14.59 4.41 10.97C4.41 7.35 7.35 4.41 10.97 4.41C14.59 4.41 17.54 7.35 17.54 10.97C17.54 14.59 14.59 17.54 10.97 17.54Z" fill="grey"/>
                    </svg>
                </span>

                <template v-if="this.completionResults.length > 0">
                    <div class="dropdown-menu" id="dropdown-menu-completion" role="menu">
                        <div class="dropdown-content">
                            <template v-for="(result, index) in this.completionResults" :key="index">
                                <a @click="inputCategorieSelection(result.id)" class="dropdown-item completion-line">{{result.nom}}</a>
                                <template v-if="this.completionResults[index+1]">
                                    <hr class="dropdown-divider">
                                </template>
                            </template>
                        </div>
                    </div>
                </template>
            </div>
        </div>

        <!-- DESKTOP MODE -->
        <div id="navbar-menu" class="navbar-menu is-hidden-mobile">
            <div class="navbar-start">
                <a @click="resetNavigation()" class="navbar-item-cust navbar-elem navbar-effect-elem">
                    <svg class="navbar-icon-menu-thi" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.09 4.83C9.28891 4.83 9.47967 4.75098 9.62033 4.61033C9.76098 4.46968 9.84 4.27891 9.84 4.08C9.84 3.88109 9.76098 3.69032 9.62033 3.54967C9.47967 3.40902 9.28891 3.33 9.09 3.33H5.62C5.42189 3.33259 5.23262 3.41244 5.09253 3.55254C4.95243 3.69263 4.87259 3.88189 4.87 4.08V20.2C4.87259 20.3981 4.95243 20.5874 5.09253 20.7275C5.23262 20.8676 5.42189 20.9474 5.62 20.95H9.09C9.28891 20.95 9.47967 20.871 9.62033 20.7303C9.76098 20.5897 9.84 20.3989 9.84 20.2C9.84 20.0011 9.76098 19.8103 9.62033 19.6697C9.47967 19.529 9.28891 19.45 9.09 19.45H6.37V4.83H9.09Z" fill="white"/>
                        <path d="M17.78 3.3L12.78 2.05C12.5173 1.98257 12.2426 1.97641 11.9771 2.03201C11.7116 2.08761 11.4625 2.20348 11.2489 2.37067C11.0353 2.53786 10.863 2.7519 10.7453 2.99627C10.6276 3.24063 10.5676 3.50878 10.57 3.78V20.21C10.5687 20.4446 10.6138 20.6771 10.7026 20.8942C10.7915 21.1114 10.9224 21.3088 11.0878 21.4751C11.2532 21.6415 11.4499 21.7735 11.6665 21.8636C11.8831 21.9536 12.1154 22 12.35 22C12.4987 21.9997 12.6467 21.9795 12.79 21.94L17.79 20.69C18.1675 20.5938 18.5031 20.3763 18.7451 20.0711C18.9872 19.7658 19.1224 19.3895 19.13 19V5C19.124 4.60742 18.9883 4.22785 18.7442 3.92039C18.5 3.61292 18.161 3.3948 17.78 3.3ZM13.62 13.37C13.17 13.37 12.62 13.01 12.62 12C12.62 10.99 13.14 10.62 13.62 10.62C14.1 10.62 14.62 10.98 14.62 12C14.62 13.02 14.08 13.37 13.62 13.37Z" fill="white"/>
                    </svg>
                    Accueil
                </a>

                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link navbar-elem">
                        <svg class="navbar-icon-menu" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3.78003 12.75H6.11002V20.22C6.11002 21.2 6.91005 22 7.89005 22H8.92004C9.90004 22 10.69 21.2 10.69 20.22V12.75H17.48C17.69 12.75 17.9 12.66 18.04 12.5L20.78 9.41C21.04 9.13 21.04 8.7 20.78 8.42L18.04 5.33C17.9 5.17 17.69 5.08 17.48 5.08H10.69V3.78C10.69 2.8 9.90004 2 8.92004 2H7.89005C6.91005 2 6.11002 2.8 6.11002 3.78V5.08H3.78003C3.36003 5.08 3.03003 5.42 3.03003 5.83V12C3.03003 12.41 3.36003 12.75 3.78003 12.75ZM7.61002 3.78C7.61002 3.63 7.74005 3.5 7.89005 3.5H8.92004C9.07004 3.5 9.19003 3.63 9.19003 3.78V5.08H7.61002V3.78ZM7.61002 12.75H9.19003V20.22C9.19003 20.37 9.07004 20.5 8.92004 20.5H7.89005C7.74005 20.5 7.61002 20.37 7.61002 20.22V12.75Z" fill="white"/>
                        </svg>
                        CATÉGORIE
                    </a>

                    <div class="navbar-dropdown">
                        <template v-if="this.categories.length > 0">
                            <template v-for="(categorie, index) in this.categories" :key="index">
                                <a @click="goToThread(categorie.id)" class="navbar-item navbar-line">
                                    • {{categorie.nom}}
                                </a>
                            </template>
                        </template>
                        <template v-else>
                            <a class="navbar-item">Aucune catégorie pour le moment.</a>
                        </template>
                    </div>
                </div>

                <a @click="getSelection()" class="navbar-item-cust navbar-elem navbar-effect-elem">
                    <svg class="navbar-icon-menu-sec" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M11.13 11.17L14.25 9.76L12.87 12.83L9.72 14.32L11.13 11.17Z" fill="white"/>
                        <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM15.7 10.17L14.19 13.49C14.05 13.8 13.8 14.05 13.49 14.19L10.17 15.7C9.98 15.79 9.78 15.83 9.58 15.83C9.21 15.83 8.86 15.69 8.58 15.42C8.16 15 8.05 14.37 8.3 13.83L9.81 10.51C9.95 10.2 10.2 9.95 10.51 9.81L13.83 8.3C14.37 8.05 15 8.16 15.42 8.58C15.84 9 15.95 9.63 15.7 10.17Z" fill="white"/>
                    </svg>
                    Notre sélection
                </a>

                <a @click="getBestOf()" class="navbar-item-cust navbar-elem navbar-effect-elem">
                    <svg class="navbar-icon-menu-sec" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19.3 4.05H17.92V2.75C17.9213 2.65114 17.9029 2.55301 17.8656 2.4614C17.8284 2.3698 17.7732 2.28659 17.7033 2.21667C17.6334 2.14676 17.5502 2.09156 17.4586 2.05435C17.367 2.01714 17.2689 1.99865 17.17 2H6.88999C6.69108 2 6.50031 2.07902 6.35966 2.21967C6.21901 2.36032 6.13999 2.55109 6.13999 2.75V4.05H4.70999C4.25541 4.03377 3.81291 4.19826 3.47932 4.50749C3.14573 4.81672 2.94822 5.2455 2.92999 5.7V8.93C2.93116 9.15616 2.98086 9.37944 3.07575 9.58473C3.17063 9.79003 3.30849 9.97257 3.47999 10.12L7.14999 13.38C7.62118 14.053 8.23252 14.6161 8.942 15.0304C9.65149 15.4447 10.4423 15.7004 11.26 15.78V17.39H8.81999C8.37939 17.3929 7.95553 17.5592 7.63042 17.8566C7.30532 18.154 7.10206 18.5614 7.05999 19L6.90999 20C6.8768 20.2521 6.898 20.5084 6.97217 20.7516C7.04635 20.9948 7.17177 21.2193 7.33999 21.41C7.50597 21.5985 7.71078 21.7488 7.94036 21.8507C8.16995 21.9525 8.41886 22.0035 8.66999 22H15.39C15.6418 21.9991 15.8905 21.9448 16.1198 21.8407C16.349 21.7365 16.5536 21.585 16.7199 21.3959C16.8863 21.2069 17.0106 20.9847 17.0847 20.7441C17.1589 20.5035 17.1811 20.2499 17.15 20L17 19C16.94 18.5749 16.7293 18.1855 16.4063 17.9028C16.0832 17.6202 15.6693 17.463 15.24 17.46H12.78V15.8C13.6289 15.7205 14.4491 15.4509 15.1796 15.0112C15.9102 14.5715 16.5323 13.973 17 13.26L20.52 10.13C20.6913 9.9802 20.8288 9.7958 20.9236 9.58896C21.0184 9.38212 21.0683 9.15753 21.07 8.93V5.7C21.0623 5.4754 21.0103 5.25452 20.9171 5.05C20.824 4.84549 20.6914 4.66135 20.527 4.5081C20.3626 4.35486 20.1696 4.23552 19.9591 4.15692C19.7486 4.07831 19.5246 4.04198 19.3 4.05ZM4.42999 8.93V5.7C4.42999 5.65 4.53999 5.55 4.70999 5.55H6.13999V10.14C6.13999 10.26 6.13999 10.37 6.13999 10.48L4.42999 8.93ZM14.43 8.53L13.77 9.18L13.92 10.09C13.9447 10.2281 13.9306 10.3703 13.8794 10.5009C13.8283 10.6315 13.7419 10.7454 13.63 10.83C13.5065 10.9278 13.3569 10.9869 13.2 11C13.081 10.9986 12.9641 10.9676 12.86 10.91L12 10.45L11.18 10.88C11.0568 10.9462 10.9175 10.9765 10.7779 10.9677C10.6383 10.9589 10.5039 10.9112 10.39 10.83C10.2763 10.7466 10.188 10.6333 10.135 10.5026C10.082 10.3719 10.0664 10.229 10.09 10.09L10.25 9.18L9.57999 8.53C9.47948 8.43206 9.40846 8.30789 9.37501 8.17159C9.34157 8.0353 9.34703 7.89235 9.39078 7.75901C9.43454 7.62567 9.51482 7.50727 9.62252 7.41729C9.73021 7.32731 9.86099 7.26935 9.99999 7.25L11 7.11L11.41 6.28C11.4805 6.16411 11.5796 6.06832 11.6978 6.00185C11.816 5.93537 11.9494 5.90046 12.085 5.90046C12.2206 5.90046 12.354 5.93537 12.4722 6.00185C12.5904 6.06832 12.6895 6.16411 12.76 6.28L13.17 7.11L14.09 7.25C14.2275 7.27103 14.3564 7.32986 14.4623 7.41992C14.5683 7.50998 14.6471 7.62773 14.69 7.76C14.7288 7.89781 14.7267 8.0439 14.6841 8.18057C14.6415 8.31724 14.5602 8.43862 14.45 8.53H14.43ZM15.23 18.91C15.2967 18.9096 15.3612 18.9339 15.411 18.9782C15.4609 19.0225 15.4926 19.0837 15.5 19.15L15.65 20.15C15.654 20.1895 15.6499 20.2294 15.6378 20.2673C15.6258 20.3051 15.6061 20.3401 15.58 20.37C15.5552 20.4018 15.5232 20.4274 15.4868 20.4448C15.4503 20.4621 15.4104 20.4708 15.37 20.47H8.66999C8.63104 20.4708 8.59248 20.4621 8.55764 20.4447C8.52279 20.4273 8.49271 20.4016 8.46999 20.37C8.43997 20.3428 8.41768 20.3081 8.40539 20.2694C8.3931 20.2308 8.39124 20.1896 8.39999 20.15L8.53999 19.15C8.55158 19.0837 8.58585 19.0235 8.63693 18.9798C8.68801 18.936 8.75273 18.9113 8.81999 18.91H15.23ZM19.52 9L17.91 10.44C17.91 10.34 17.91 10.24 17.91 10.14V5.55H19.3C19.47 5.55 19.57 5.65 19.57 5.7L19.52 9Z" fill="white"/>
                    </svg>
                    MEILLEUR DE 2022
                </a>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="control has-icons-right">
                        <input 
                        v-on:keyup="inputCompletion()"
                        v-model="this.clientInput"
                        class="input is-medium search-bar" type="email" placeholder="Recherche ...">
                        <span class="icon is-medium is-right search-button">
                            <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M10.97 5.91C8.18003 5.91 5.91003 8.18 5.91003 10.97C5.91003 13.76 8.18003 16.04 10.97 16.04C13.77 16.04 16.04 13.76 16.04 10.97C16.04 8.18 13.77 5.91 10.97 5.91Z" fill="grey"/>
                                <path d="M21.78 20.72L17.82 16.76C19.14 15.19 19.94 13.18 19.94 10.97C19.94 6.03 15.92 2 10.97 2C6.03 2 2 6.03 2 10.97C2 15.92 6.03 19.94 10.97 19.94C13.18 19.94 15.2 19.14 16.76 17.82L20.72 21.78C20.87 21.93 21.06 22 21.25 22C21.44 22 21.63 21.93 21.78 21.78C22.07 21.49 22.07 21.01 21.78 20.72ZM10.97 17.54C7.35 17.54 4.41 14.59 4.41 10.97C4.41 7.35 7.35 4.41 10.97 4.41C14.59 4.41 17.54 7.35 17.54 10.97C17.54 14.59 14.59 17.54 10.97 17.54Z" fill="grey"/>
                            </svg>
                        </span>

                        <template v-if="this.completionResults.length > 0">
                            <div class="dropdown-menu" id="dropdown-menu-completion" role="menu">
                                <div class="dropdown-content">
                                    <template v-for="(result, index) in this.completionResults" :key="index">
                                        <a @click="inputCategorieSelection(result.id)" class="dropdown-item completion-line">{{result.nom}}</a>
                                        <template v-if="this.completionResults[index+1]">
                                            <hr class="dropdown-divider">
                                        </template>
                                    </template>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'Navbar',
    data() {
      return {
        clientInput: null,
        phoneMenuBurger: false,
      }
    },
    computed: mapState ([
        'categories',
        'completionResults'
    ]),
    components: {
    },
    methods: {
        phoneMenu() {
          if (this.phoneMenuBurger) {
            this.phoneMenuBurger = false;
          } else {
            this.phoneMenuBurger = true;
          }
        },

        goToThread(id) {
            this.$store.dispatch('perCategories', {'id':id, infoPage:null})
            .then({
                this:this.$router.push({ name: 'Accueil'})
            });
        },

        getBestOf() {
            this.$store.dispatch('getBestOf')
            .then({
                this:this.$router.push({ name: 'Accueil'})
            });
        },

        getSelection() {
            this.$store.dispatch('getSelection')
            .then({
                this:this.$router.push({ name: 'Accueil'})
            });
        },

        resetNavigation() {
            this.$store.dispatch('lastEntries')
            .then({
                this:this.$router.push({ name: 'Accueil'})
            });
        },

        inputCompletion() {
            if (this.clientInput.length >= 2) {
                this.$store.dispatch('inputSearchCompletion', this.clientInput);
            } else {
                this.$store.dispatch('resetSearchCompletion');
            }
        },

        inputCategorieSelection(id) {
            this.$store.dispatch('resetSearchCompletion');
            this.clientInput = null;
            this.$router.push({ name: 'AnnonceDetail', params: {pk: id} });
        }
    }
}
</script>

<style lang="scss">
    @font-face {
        font-family: "leagueSpartan";
        src: url("../../public/fonts/LeagueSpartan-Bold.otf");
    }

    #navMenu {
      height:auto!important;
      padding: 10% 15%!important;

        a {
            font-weight:bold;
        }

        p {
            margin-bottom:5%;
        }

        hr {
            background-color:#d1d0cd;
        }

        #connexion-btn-phoneMenu {
        margin-right:3%;
        color:#01796F!important;
        border-color:#01796F;
        font-size: .8em!important;
        }

        .phone-menu {
        color:#4a4a4a;
        font-weight:bold;
        cursor:pointer;
        }

        .icon-phoneMenu {
            color:#01796F;
            font-size:1.6em;
            margin-right:2%;
        }

    }

    #dropdown-menu-completion {
        display: block;
        max-height: 400px;
        width: 343px;
        overflow: auto;
    }

    #dropdown-menu-completion div {
        background-color: #f6f6f6;
        border-radius: 10px;
    }

    #dropdown-menu-completion div a {
        color:#6b6bc7!important;
    }

    #dropdown-menu-completion div a:hover {
        color:black!important;
    }

    .completion-line {
        white-space: break-spaces!important;
    }

    .navbar-icon-menu {
        margin-top:-9%;
        width: 40px;
    }

    .navbar-icon-menu-sec {
        margin-top:-5%;
        margin-right:2%;
        width: 40px;
    }

    .navbar-icon-menu-thi {
        margin-top:-7%;
        margin-right:2%;
        width: 40px;
    }

    .navbar-elem {
        font-size:1.2em;
        font-family: 'leagueSpartan';
        color:black!important;
    }

    .navbar-link:hover, .navbar-item:hover {
        background-color:#A6A6EF!important;
    }

    #navbar-menu {
        margin-left:5%;
    }

    .navbar-line {
        font-size:1.3em;
    }

    .search-button {
        cursor: pointer;
    }

    .navbar-item-cust {
        align-items: center;
        display: flex;
        margin-right:3%;
        width: auto;
        white-space: nowrap;
    }

    @keyframes anim2 {
        0% {
            opacity: 1;
            transform: translateY(px);
        }
        25% {
            opacity: 0;
            transform: translateY(-10px);
        }
        50% {
            opacity: 1;
            transform: translateY(0px);
        }
        75% {
            opacity: 0;
            transform: translateY(10px);
        }
        100% {
            opacity: 1;
            transform: translateY(0px);
        }
    }

    .navbar-effect-elem {
        display: block;
        //height: 100%;
        //margin-right: 30px;
        //font-size: 20px;
        position: relative;
        display: flex;
        align-items: center;
        color: #fff;
        text-transform: uppercase;
        //text-shadow: 0 0 15px #8e54e9;
        transition: all 300ms cubic-bezier(0.075, 0.82, 0.165, 1);
    }

    .navbar-effect-elem:after,
    .navbar-effect-elem:before {
        content: "";
        position: absolute;
        width: 0%;
        display: block;
        height: 6px;
        transition: all 0.3s ease;
        margin-top: 2px;
        transition: all 300ms ease-in;
    }

    .navbar-effect-elem:after {
        bottom: 25%;
        left: 0;
    }

    .navbar-effect-elem:before {
        top: 25%;
        right: 0;
    }

    .navbar-effect-elem:hover::after {
        width: 100%;
        height: 6px;
        bottom: 25%;
        background-color: #fff;
    }
    .navbar-effect-elem:hover::before {
        width: 100%;
        height: 6px;
        top: 25%;
        background-color: #fff;
    }

    .search-bar {
        border-radius:35px!important;
        width: 350px!important;
    }


    @media only screen and (max-width:768px) {
        .navbar-line {
            font-size: 1em;
        } 

        .navbar-icon-menu-sandwich {
            width: 30px;
            margin-bottom:-2.5%;
        }

        .navbar-dropdown {
            margin-top:-7%!important;
        }

        #navMenu a {
            font-weight: normal;
        }

        #navMenu p {
            margin-bottom: 7%!important;
        }

        .search-bar {
            font-size: 1em!important;
        }

        .search-button {
            top:-5px!important;
        }

        #dropdown-menu-completion {
            width: 100%;
            max-height: 290px ​!important;
        }
    }   

    @media only screen and (max-width: 350px) {
        .navbar-icon-menu-sandwich {
            margin-bottom:-3%;
        }
    }


</style>

