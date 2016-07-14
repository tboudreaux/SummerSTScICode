from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[178.748625,28.134778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_115459.67+280805.2/sdB_sdssj_115459.67+280805.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_115459.67+280805.2/sdB_sdssj_115459.67+280805.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
