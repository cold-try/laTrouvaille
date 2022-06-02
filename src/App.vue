<template>
  <div>
    <Navbar/>
    <router-view />
    <Footer/>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App',
  created() {
    this.$store.dispatch('getCategories');
  },
  components: {
    Navbar,
    Footer
  },
  methods: {
  }
}
</script>

<style lang="scss">
</style>