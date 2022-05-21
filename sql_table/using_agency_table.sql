USE [frpp_public]
GO

/****** Object:  Table [dbo].[UsingAgency]    Script Date: 21.05.2022 20:23:00 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[UsingAgency](
	[using_agency_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[using_agency_name] [nvarchar](50) NULL,
	[using_agency_code] [int] NULL,
 CONSTRAINT [PK_UsingAgency] PRIMARY KEY CLUSTERED 
(
	[using_agency_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


