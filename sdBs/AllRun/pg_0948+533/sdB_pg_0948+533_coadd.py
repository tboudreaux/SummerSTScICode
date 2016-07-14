from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[147.857542,53.158533],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0948+533/sdB_pg_0948+533_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0948+533/sdB_pg_0948+533_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
