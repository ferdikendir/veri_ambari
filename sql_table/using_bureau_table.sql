USE [frpp_public]
GO

/****** Object:  Table [dbo].[UsingBureau]    Script Date: 21.05.2022 20:23:14 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[UsingBureau](
	[using_bureau_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[using_bureau_name] [nvarchar](max) NULL,
	[using_bureau_code] [int] NULL,
 CONSTRAINT [PK_UsingBureau] PRIMARY KEY CLUSTERED 
(
	[using_bureau_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


