<template>
  <div>
    <a-form :label-col="{ span: 4 }" :wrapper-col="{ span: 16 }" :form="form" @submit="onSubmit">
      <a-form-item>
        <a-input-group compact>
          <a-select v-model:value="dropdownValue" style="width:120px">
            <a-select-option value="uid">{{ $t('queryUserInfo.dropdown.uid') }}</a-select-option>
            <a-select-option value="mobile">{{ $t('queryUserInfo.dropdown.mobile') }}</a-select-option>
          </a-select>
          <a-input type="text" style="width: 50%" :placeholder="$t('queryUserInfo.uid.placeholder')" v-decorator="[
            `uids`,
            {
              rules: [
                {
                  required: true,
                  message: '请输入',
                },
              ],
            },
          ]" />
        </a-input-group>
      </a-form-item>

      <a-form-item>
        <a-button type="primary" html-type="submit">操作</a-button>
        <a-button style="margin-left: 10px" @click="resetForm">重置</a-button>
      </a-form-item>
    </a-form>

    <a-table :dataSource="dataSource" :columns="columns" bordered :loading="tableLoading">
      <template #title>{{ tableTitle }}</template>
    </a-table>

  </div>
</template>

<script>
import { getAccountInfo } from '@/api/certification'
import { message } from 'ant-design-vue'
export default {
  name: 'QueryUserInfo',
  data() {
    return {
      form: this.$form.createForm(this, { name: 'QueryUserInfo' }),
      uids: '',
      dropdownValue: 'uid',

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
          title: '手机号',
          dataIndex: 'mobile',
          key: 'mobile',
          align: 'center'
        },
        {
          title: '昵称',
          dataIndex: 'nickname',
          key: 'nickname',
          align: 'center'
        },
        {
          title: '注册时间',
          dataIndex: 'registerTime',
          key: 'registerTime',
          align: 'center'
        },
        {
          title: '是否加V',
          dataIndex: 'verify',
          key: 'verify',
          align: 'center'
        },
        {
          title: '返回信息',
          dataIndex: 'msg',
          key: 'msg',
          align: 'center'
        },
      ]
    }
  },
  methods: {
    resetForm() {
      this.form.resetFields()
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

            getAccountInfo({
              number: _this.uids,
              mode: _this.dropdownValue
            }).then(res => {
              if (res.code === 200 && res?.data) {
                let successCount = 0
                res?.data?.map((item, index) => {
                  _this.dataSource.push({
                    key: (index + 1) + '',
                    uid: item?.uid || '-',
                    mobile: item?.mobile || '-',
                    nickname: item?.nickname || '-',
                    registerTime: item?.registerTime || '-',
                    verify: item?.verify ? '是' : '否',
                    msg: item?.msg || '-',
                  })
                  if (item?.profileVerify) {
                    successCount += 1
                  }
                })
                _this.tableTitle = `请求${_this.dropdownValue}数量：${_this.dataSource.length}，成功数量：${successCount}`
              } else {
                message.error(res?.msg || '出错了，请@张柔')
                _this.tableTitle = res?.msg || '出错了，请@张柔'
              }
              _this.tableLoading = false
            }).catch(err => {
              message.error(err?.msg || '出错了，请@张柔')
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