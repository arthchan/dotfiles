return {
	"nvim-neo-tree/neo-tree.nvim",
	branch = "v3.x",
	dependencies = {
		"nvim-lua/plenary.nvim",
		"nvim-tree/nvim-web-devicons",
		"MunifTanjim/nui.nvim",
		"s1n7ax/nvim-window-picker",
	},
	config = function()
		require("neo-tree").setup{}
		vim.keymap.set("n", "<leader>b", ":Neotree toggle<CR>", { desc = "Neotree: Toggle Neotree" })
	end,
}