from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[229.765208,0.017778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_151903.65+000104.0/sdB_SDSSJ910_151903.65+000104.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_151903.65+000104.0/sdB_SDSSJ910_151903.65+000104.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
