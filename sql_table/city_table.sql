USE [frpp_public]
GO

/****** Object:  Table [dbo].[City]    Script Date: 21.05.2022 20:20:29 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[City](
	[city_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[city_name] [nvarchar](50) NULL,
	[city_code] [int] NULL,
	[zip_code] [nvarchar](50) NULL,
	[country_id] [int] NULL,
 CONSTRAINT [PK_City] PRIMARY KEY CLUSTERED 
(
	[city_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


