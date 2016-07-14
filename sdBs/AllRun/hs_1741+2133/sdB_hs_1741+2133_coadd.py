from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[265.829417,21.543939],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_1741+2133/sdB_hs_1741+2133_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_1741+2133/sdB_hs_1741+2133_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
