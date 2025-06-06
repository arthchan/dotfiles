return {
	{
		"nvim-telescope/telescope.nvim",
		tag = "0.1.8",
		dependencies = {
			"nvim-lua/plenary.nvim",
			"BurntSushi/ripgrep",
			"sharkdp/fd",
	},
		opts = {},
		config = function()
			local builtin = require("telescope.builtin")
			vim.keymap.set("n", "<leader>fb", builtin.buffers, { desc = "Telescope: List buffers" })
			vim.keymap.set("n", "<leader>fd", builtin.diagnostics, { desc = "Telescope: List diagnostics" })
			vim.keymap.set("n", "<leader>ff", builtin.find_files, { desc = "Telescope: Find files" })
			vim.keymap.set("n", "<leader>fg", builtin.live_grep, { desc = "Telescope: Find by grep" })
			vim.keymap.set("n", "<leader>fh", builtin.help_tags, { desc = "Telescope: List help tags" })
			vim.keymap.set("n", "<leader>fk", builtin.keymaps, { desc = "Telescope: Find keymaps" })
			vim.keymap.set("n", "<leader>fr", builtin.resume, { desc = "Telescope: List results of previous picker" })
			vim.keymap.set("n", "<leader>fw", builtin.grep_string, { desc = "Telescope: Find current word" })
			vim.keymap.set("n", "<leader>f.", builtin.oldfiles, { desc = "Telescope: List recent files" })
		end,
	},
	{
		"nvim-telescope/telescope-ui-select.nvim",
		config = function()
			require("telescope").setup({
				extensions = {
					["ui-select"] = {
						require("telescope.themes").get_dropdown({}),
					},
				},
			})
			require("telescope").load_extension("ui-select")
		end,
	},
}
