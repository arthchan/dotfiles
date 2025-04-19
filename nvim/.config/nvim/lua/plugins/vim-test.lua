return {
	"vim-test/vim-test",
	dependencies = {
		"akinsho/toggleterm.nvim",
	},
	vim.keymap.set("n", "<leader>ta", ":TestFile<CR>", { desc = "Test.vim: Run all tests in the current file" }),
	vim.keymap.set("n", "<leader>tl", ":TestLast<CR>", { desc = "Test.vim: Run the last test" }),
	vim.keymap.set("n", "<leader>tn", ":TestNearest<CR>", { desc = "Test.vim: Run the test nearest to the cursor" }),
	vim.keymap.set("n", "<leader>ts", ":TestSuite<CR>", { desc = "Test.vim: Run the whole test suite" }),
	vim.keymap.set("n", "<leader>tv", ":TestVisit<CR>", { desc = "Test.vim: Visit the test file" }),
	vim.cmd("let test#strategy = 'toggleterm'"),
}
