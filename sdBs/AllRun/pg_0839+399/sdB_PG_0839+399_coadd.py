from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[130.802917,39.747253],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_0839+399/sdB_PG_0839+399_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_0839+399/sdB_PG_0839+399_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
