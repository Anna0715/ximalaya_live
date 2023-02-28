<template>
  <a-result status="404" title="网页暂未开发" >
    <template #extra>
      <a-button type="primary" @click="toHome">
        回到首页
      </a-button>
    </template>
  </a-result>
</template>

<script>
export default {
  name: 'Exception404',
  methods: {
    toHome () {
      this.$router.push({ path: '/' })
    }
  }
}
</script>
