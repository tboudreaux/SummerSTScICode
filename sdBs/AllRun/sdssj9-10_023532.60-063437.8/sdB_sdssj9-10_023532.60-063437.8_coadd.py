from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[38.885833,-6.577167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_023532.60-063437.8/sdB_sdssj9-10_023532.60-063437.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_023532.60-063437.8/sdB_sdssj9-10_023532.60-063437.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
