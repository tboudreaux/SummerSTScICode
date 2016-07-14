from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[229.847505,-33.712608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_TON_S183/sdB_TON_S183_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_TON_S183/sdB_TON_S183_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
