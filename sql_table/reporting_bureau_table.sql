USE [frpp_public]
GO

/****** Object:  Table [dbo].[ReportingBureau]    Script Date: 21.05.2022 20:22:10 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ReportingBureau](
	[reporting_bureau_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[reporting_bureau_name] [nvarchar](100) NULL,
	[reporting_bureau_code] [int] NULL,
 CONSTRAINT [PK_ReportingBureau] PRIMARY KEY CLUSTERED 
(
	[reporting_bureau_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


