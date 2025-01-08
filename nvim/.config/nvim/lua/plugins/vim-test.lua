return {
	"vim-test/vim-test",
	dependencies = {
		"akinsho/toggleterm.nvim",
	},
	vim.keymap.set("n", "<leader>T", ":TestFile<CR>", { desc = "Test: Run all tests in the current file" }),
	vim.keymap.set("n", "<leader>tn", ":TestNearest<CR>", { desc = "Test: Run the test nearest to the cursor" }),
	vim.keymap.set("n", "<leader>ts", ":TestSuite<CR>", { desc = "Test: Run the whole test suite" }),
	vim.keymap.set("n", "<leader>tl", ":TestLast<CR>", { desc = "Test: Run the last test" }),
	vim.keymap.set("n", "<leader>tv", ":TestVisit<CR>", { desc = "Test: Visit the test file" }),
	vim.cmd("let test#strategy = 'toggleterm'"),
}
