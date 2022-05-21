USE [frpp_public]
GO

/****** Object:  Table [dbo].[County]    Script Date: 21.05.2022 20:21:36 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[County](
	[county_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[county_name] [nvarchar](50) NULL,
	[county_code] [int] NULL,
 CONSTRAINT [PK_County] PRIMARY KEY CLUSTERED 
(
	[county_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

