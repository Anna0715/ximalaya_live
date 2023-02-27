<template>
  <div>
    <a-form :label-col="{ span: 4 }" :wrapper-col="{ span: 16 }" :form="form" @submit="onSubmit">
      <a-form-item :label="$t('certification.uid')">
        <a-input type="text" :placeholder="$t('certification.uid.placeholder')" v-decorator="[
          `uids`,
          {
            rules: [
              {
                required: true,
                message: '请输入uid',
              },
            ],
          },
        ]" />
      </a-form-item>

      <a-form-item :label="$t('certification.vedio.check')">
        <a-switch :checked="openVedio" @change="onVedioChange" />
      </a-form-item>
      <a-form-item :label="$t('certification.sale.check')">
        <a-switch :checked="openSale" @change="onSaleChange" />
      </a-form-item>
      <a-form-item :label="$t('certification.response.textarea')">
        <a-textarea :rows="4" v-decorator="[
          `cookies`,
          {
            rules: [
              {
                required: true,
                message: '请输入cookies',
              },
            ],
          },
        ]" />
      </a-form-item>

      <a-form-item :wrapper-col="{ span: 14, offset: 4 }">
        <a-button type="primary" html-type="submit">操作</a-button>
        <a-button style="margin-left: 10px" @click="resetForm">重置</a-button>
      </a-form-item>
    </a-form>

    <a-table :dataSource="dataSource" :columns="columns" bordered :loading="tableLoading">
      <template #title>{{ tableTitle }}</template>
      <template slot="isCertification" slot-scope="item">
        <a-icon type="check-circle" theme="filled" style="color:#52c41a" v-if="item.isCertification === 'success'" />
        <a-icon type="close-circle" theme="filled" v-if="item.isCertification === 'fail'" />
      </template>
      <template slot="openVedio" slot-scope="item">
        <a-icon type="check-circle" theme="filled" style="color:#52c41a" v-if="item === 'success'" />
        <a-icon type="close-circle" theme="filled" v-if="item === 'fail'" />
        <span v-if="item === 'false'">/</span>
      </template>
      <template slot="openSale" slot-scope="item">
        <a-icon type="check-circle" theme="filled" style="color:#52c41a" v-if="item === 'success'" />
        <a-icon type="close-circle" theme="filled" v-if="item === 'fail'" />
        <span v-if="item === 'false'">/</span>
      </template>
    </a-table>

  </div>
</template>

<script>
import { addVprofileVerify } from '@/api/certification'
import { message } from 'ant-design-vue';
export default {
  name: 'Certification',
  data() {
    return {
      form: this.$form.createForm(this, { name: 'Certification' }),
      openVedio: false,
      openSale: false,
      uids: '',

      dataSource: [],
      tableTitle: '请求uid数量：0，成功数量：0',
      tableLoading: false,
      columns: [
        {
          title: 'uid',
          dataIndex: 'uid',
          key: 'uid',
          align: 'center'
        },
        {
          title: '实名认证',
          slots: {
            title: 'isCertification',
          },
          scopedSlots: { customRender: 'isCertification', },
          align: 'center'
        },
        {
          title: '视频权限',
          dataIndex: 'openVedio',
          slots: {
            title: 'openVedio',
          },
          scopedSlots: { customRender: 'openVedio', },
          align: 'center'
        },
        {
          title: '卖货权限',
          dataIndex: 'openSale',
          slots: {
            title: 'openSale',
          },
          scopedSlots: { customRender: 'openSale', },
          align: 'center'
        }
      ]
    }
  },
  methods: {
    onVedioChange() {
      this.openVedio = !this.openVedio
    },
    onSaleChange() {
      this.openSale = !this.openSale
    },
    resetForm() {
      this.form.resetFields()
      this.openVedio = false
      this.openSale = false
      this.dataSource = []
      this.tableTitle = ''
    },
    onSubmit(e) {
      e.preventDefault()
      const _this = this
      this.form.validateFields((error, values) => {
        console.log('error', error, values)
        if (!error) {
          _this.uids = values?.uids
          if (_this.uids) {
            _this.dataSource = []
            _this.tableLoading = true
            addVprofileVerify({
              uid: _this.uids,
              isOpenlvb: _this.openVedio,
              isOpengoods: _this.openSale,
              cookie: values?.cookies
            }).then(res => {
              if (res.code === 200 && res?.data) {
                let successCount = 0
                res?.data?.map((item, index) => {
                  _this.dataSource.push({
                    key: (index + 1) + '',
                    uid: item?.uid,
                    isCertification: item?.profileVerify,
                    openSale: item?.OpenGoods,
                    openVedio: item?.Openlv
                  })
                  if (item?.profileVerify) {
                    successCount += 1
                  }
                })
                _this.tableTitle = `请求uid数量：${_this.dataSource.length}，成功数量：${successCount}`
              } else {
                message.error(res?.msg || '出错了，请@张柔');
                _this.tableTitle = res?.msg || '出错了，请@张柔'
              }
              _this.tableLoading = false
            }).catch(err => {
              message.error(err?.msg || '出错了，请@张柔');
              _this.tableTitle = err?.msg || '出错了，请@张柔'
              _this.tableLoading = false
            })
          }
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>
.item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.item-uid-label {
  margin-right: 10px;
}
</style>
