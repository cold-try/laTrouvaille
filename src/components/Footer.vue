<template>
    <footer class="footer">
        <div class="content has-text-centered">
            <p>
                <strong style="color:#A6A6EF">La Trouvaille</strong>, 2022 - France ; Amazon Affiliate Disclosure
            </p>
        </div>
    </footer>
</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'Footer',
    data() {
      return {
      }
    },
    computed: mapState ([
    ]),
    components: {
    },
    methods: {
    }
}
</script>

<style lang="scss">
    footer {
        margin-top:5%;
        background-color: #222!important;
        color:white!important;
    }

</style>