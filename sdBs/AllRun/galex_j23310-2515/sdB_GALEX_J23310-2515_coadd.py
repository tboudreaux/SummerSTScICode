from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[352.765333,-25.263592],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J23310-2515/sdB_GALEX_J23310-2515_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J23310-2515/sdB_GALEX_J23310-2515_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()