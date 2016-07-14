from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[10.838292,44.573456],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0040+4417/sdB_hs_0040+4417_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0040+4417/sdB_hs_0040+4417_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
