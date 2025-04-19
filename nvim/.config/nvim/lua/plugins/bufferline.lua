return {
	"akinsho/bufferline.nvim",
	version = "*",
	dependencies = "nvim-tree/nvim-web-devicons",
	config = function()
		require("bufferline").setup{}
		vim.keymap.set("n", "<A-h>", ":bp<CR>", { desc = "Bufferline: Go to previous buffer" })
		vim.keymap.set("n", "<A-l>", ":bn<CR>", { desc = "Bufferline: Go to next buffer" })
		vim.keymap.set("n", "<A-q>", ":bd<CR>", { desc = "Bufferline: Close buffer" })
	end,
}
