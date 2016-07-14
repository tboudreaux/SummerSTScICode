from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[62.457042,-28.334328],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_TONS_403/sdB_TONS_403_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_TONS_403/sdB_TONS_403_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
