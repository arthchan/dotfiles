return {
	{
		"akinsho/toggleterm.nvim",
		version = "*",
		config = true,
		vim.keymap.set("t", "<esc>", "<C-\\><C-n>", { desc = "ToggleTerm: Exit terminal mode" }),
		vim.keymap.set("n", "<leader><CR>", ":ToggleTerm<CR>", { desc = "ToggleTerm: Toggle terminal" }),
		vim.keymap.set("t", "<leader><CR>", "<C-\\><C-n><C-w>q", { desc = "ToggleTerm: Close terminal" }),
	},
}
