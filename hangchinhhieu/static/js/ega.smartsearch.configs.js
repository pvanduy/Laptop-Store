const EGASmartSearchConfigs = {
	settings: {
		isEnabled: false,
    // color
		colorBg: '#FFFFFF',
		colorBgHover: '#F7F7F7',
		colorLabelBg: '#F7F7F7',
		colorLabelText: '#A0A0A0',
		colorItemBorder: '#EEEEEE',
		colorItemTextTitle: '#0288D1',
		colorItemTextPrice: '#014E70',
		colorItemTextCompareAtPrice: '#A7A7A7',
		colorItemTextSku: '#747474',
		colorItemTextDescription: '#747474',
		colorItemTextViewAll: '#0288D1',
		colorHeaderText: '#A0A0A0',
		colorLoading: '#ff0000',
		// general
		searchAccuracy: 'all',
		isFixedSearch: 'absolute',
		searchWidth: '380px',
		searchHeight: '500px',
		searchView:	'list',
    
		// product
		productSortby: '',
		displayProductDescription: false,
		productLimit: 3,

		// article
		displayArticle: false,
		displayArticleDescription: false,
		articleLimit: 3
	},
	CONSTANT: {
		shopDomain: '',
		searchView: 'ega.smartsearch.json',
		textHeaderSectionTitle: 'Kết quả tìm kiếm cho ',
		textProductSectionTitle: 'Sản phẩm',
		textArticleSectionTitle: 'Bài viết',
		notFound: 'Không tìm thấy kết quả',
		textFrom: 'Từ ',
		textShowAll: 'Hiển thị sản phẩm có chứa '
	}
}
var EGASmartSearchRegister = {
	js: [
		"//theme.hstatic.net/1000233206/1000806987/14/ega.smartsearch.js?v=1528"
	]
}