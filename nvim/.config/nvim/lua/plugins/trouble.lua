return {
	"folke/trouble.nvim",
	opts = {},
	cmd = "Trouble",
	keys = {
		{
			"<leader>xl",
			"<cmd>Trouble loclist toggle<cr>",
			desc = "Trouble: Toggle location list",
		},
		{
			"<leader>xq",
			"<cmd>Trouble qflist toggle<cr>",
			desc = "Trouble: Toggle quickfix list",
		},
		{
			"<leader>xx",
			"<cmd>Trouble diagnostics toggle<cr>",
			desc = "Trouble: Toggle diagnostics",
		},
		{
			"<leader>xX",
			"<cmd>Trouble diagnostics toggle filter.buf=0<cr>",
			desc = "Trouble: Toggle buffer diagnostics",
		},
	},
}
