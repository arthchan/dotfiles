return {
	{
		"nvimtools/none-ls.nvim",
		config = function()
			local null_ls = require("null-ls")
			null_ls.setup({
				sources = {
					null_ls.builtins.formatting.black,
					null_ls.builtins.formatting.clang_format,
					null_ls.builtins.formatting.isort,
					null_ls.builtins.formatting.stylua,
					null_ls.builtins.formatting.yapf,
					null_ls.builtins.completion.spell,
					null_ls.builtins.diagnostics.pylint,
				},
			})
		end,
	},
	{
		"jay-babu/mason-null-ls.nvim",
		dependencies = {
			"williamboman/mason.nvim",
			"nvimtools/none-ls.nvim",
		},
		config = function()
			require("mason-null-ls").setup({
				ensure_installed = {
					"black",
					"clang_format",
					"isort",
					"stylua",
					"yapf",
					"pylint",
				},
			})
		end,
	},
}
