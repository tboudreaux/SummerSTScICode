from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[189.381292,35.905944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_123731.51+355421.4/sdB_sdssj_123731.51+355421.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_123731.51+355421.4/sdB_sdssj_123731.51+355421.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
