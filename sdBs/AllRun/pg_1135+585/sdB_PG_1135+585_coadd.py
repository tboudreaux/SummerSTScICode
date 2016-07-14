from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.475667,58.256817],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1135+585/sdB_PG_1135+585_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1135+585/sdB_PG_1135+585_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
