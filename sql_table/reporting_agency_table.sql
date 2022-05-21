USE [frpp_public]
GO

/****** Object:  Table [dbo].[ReportingAgency]    Script Date: 21.05.2022 20:21:55 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ReportingAgency](
	[reporting_agency_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[reporting_agency_name] [nvarchar](200) NULL,
	[reporting_agency_code] [int] NULL,
 CONSTRAINT [PK_Reporting] PRIMARY KEY CLUSTERED 
(
	[reporting_agency_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


