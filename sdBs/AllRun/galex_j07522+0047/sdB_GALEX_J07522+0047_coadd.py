from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[118.063167,0.786525],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J07522+0047/sdB_GALEX_J07522+0047_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J07522+0047/sdB_GALEX_J07522+0047_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()