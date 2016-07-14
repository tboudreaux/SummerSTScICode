from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[252.931042,36.779917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_165143.45+364647.7/sdB_SDSSJ_165143.45+364647.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_165143.45+364647.7/sdB_SDSSJ_165143.45+364647.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
