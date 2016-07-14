from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[358.064708,0.688344],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PB_5566/sdB_PB_5566_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PB_5566/sdB_PB_5566_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
